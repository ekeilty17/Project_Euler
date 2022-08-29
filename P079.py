"""
f=open("p079_keylog.txt",'r')

keylog = []
lines = f.readlines()
for line in lines:
   keylog += [line.split('\n')[0]]

f.close()

def numbers_contained(L):
    out = set([])
    for N in L:
        for n in N:
            out.add(int(n))
    return list(out)

def numbers_before(L):

    nums = numbers_contained(L)

    out = []
    for i in range(len(nums)):
        out += [set([])]

    for i in range(len(nums)):
        for N in L:
            if nums[i] == int(N[2]):
                out[i].add(int(N[0]))
                out[i].add(int(N[1]))
            if nums[i] == int(N[1]):
                out[i].add(int(N[0]))

    for i in range(len(out)):
        out[i] = list(out[i])

    return out

def numbers_after(L):
    
    nums = numbers_contained(L)
    
    out = []
    for i in range(len(nums)):
        out += [set([])]
    
    for i in range(len(nums)):
        for N in L:
            if nums[i] == int(N[0]):
                out[i].add(int(N[1]))
                out[i].add(int(N[2]))
            if nums[i] == int(N[1]):
                out[i].add(int(N[2]))

    for i in range(len(out)):
        out[i] = list(out[i])

    return out

print
nums = numbers_contained(keylog)
before = numbers_before(keylog)
after = numbers_after(keylog)
for i in range(len(nums)):
    print nums[i], before[i]
print
for i in range(len(nums)):
    print nums[i], after[i]
print
print
print sorted(nums, key=lambda x: len(before[nums.index(x)]))
print sorted(nums, key=lambda x: -len(after[nums.index(x)]))
"""

from itertools import product 

def isInOrder(string, pattern):
    i = 0
    for c in string: 
        if c == pattern[i]: 
            i += 1
        
        if i == len(pattern): 
            return True

    return False

# Very slow
def brute_force(keylog):

    possible_digits = [list(range(10))]
    while True:
        for password in product(*possible_digits):
            password = "".join([str(d) for d in password])
            print(password)
            for pattern in keylog:
                if not isInOrder(password, pattern):
                    break
            else:
                # only executes if we don't break
                print()
                return password
        
        possible_digits.append( list(range(10)) )


# The idea here is we can see what digits come before and come after other digits
# using this information, we can quickly construct the password
def predecessors_and_successors(keylog):
    keylog = [[int(d) for d in pattern] for pattern in keylog]
    characters = set([d for pattern in keylog for d in pattern])

    successors = {n: set([]) for n in characters}
    predecessors = {n: set([]) for n in characters}
    for n in characters:
        for pattern in keylog:
            for i in range(len(pattern)-1):
                if n == pattern[i]:
                    successors[n] = successors[n].union(set(pattern[i+1:]))

            for i in range(1, len(pattern)):
                if n == pattern[i]:
                    predecessors[n] = predecessors[n].union(set(pattern[:i]))

    # I don't know if this will work in general
    # but in this case, if you were to print out both the predecessors and successors dictionary
    # then you would easily be able to see the solution

    #password = list(sorted(characters, key=lambda n:  len(predecessors[n])))
    password = list(sorted(characters, key=lambda n: -len(successors[n])))
    password = "".join([str(d) for d in password])
    return password

def main(keylog):
    #password = brute_force(keylog)
    password = predecessors_and_successors(keylog)

    print(f"The password is:", password)
    return password

if __name__ == "__main__":
    # reading file
    with open("p079_keylog.txt",'r') as f:
        lines = f.readlines()
    
    # parsing file
    keylog = [line.strip() for line in lines]
    
    main(keylog)
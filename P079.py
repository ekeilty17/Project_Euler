
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

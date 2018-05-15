#needed to make the divisor function a bit more efficient
def divisors(n):
    if n <= 0:
        return []
    if n == 1:
        return []
    if n == 2:
        return [1]
    f = [1]
    upper_limit = n
    i = 2
    while i < upper_limit:
        if n%i == 0:
            if i == n/i:
                f += [i]
            else:
                f += [i, n/i]
            upper_limit = n/i
        i += 1
    print n
    return f

def isAbundant(n):
    if sum(divisors(n)) > n:
        return True
    return False

n = 30000
abundant = []
abun_sums = [0]*n

for i in range(0,n):
    if isAbundant(i):
        abundant += [i]

#in order to find the numbers that cannot be written as the sum of two abundant numbers, I am initializing a list with 0's and if two abundant numbers sum to a number, I insert that number at that index
for a in range(0,len(abundant)):
    for b in range(a,len(abundant)):
        if abundant[a] + abundant[b] >= n:
            break
        abun_sums[abundant[a] + abundant[b]] = abundant[a] + abundant[b]

#then all I have to do is sum the gaps, i.e. all the indeces that contain a 0
accum = 0
for i in range(0,len(abun_sums)):
    if abun_sums[i] == 0:
        accum += i

print abundant
print
print abun_sums
print
print accum

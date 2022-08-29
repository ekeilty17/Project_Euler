import math

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return 0
    if a % b == 0:
        return b
    return gcd(b, a%b)


# Actually not to bad in terms of speed
def brute_force(N, f1, f2):
    n1, d1 = f1
    n2, d2 = f2

    fractions = []
    for d in range(2, N+1):
        #print(d)
        lower = math.floor( n1/d1 * d ) + 1
        upper = math.ceil( n2/d2 * d )
        for n in range(lower, upper):
            if gcd(n, d) == 1:
                fractions.append( (n, d) )
    
    #fractions = list(sorted(fractions, key=lambda f: f[0]/f[1]))
    #print(fractions)
    return len(fractions)


# I will define "funny-addition" of fractions as    a/b (+) c/d := (a+c)/(b+d)
# You can show that a/b < (a+c)/(b+d) < c/d
# Interestingly, using funny-addition you can generate every fraction in reduced form within a range
# just by iterately funny-adding together adjacent fractions
def funny_addition(f1, f2):
    n1, d1 = f1
    n2, d2 = f2
    return (n1+n2) , (d1+d2)

# To do this efficiently is actually a little tricky
# Take d = 7, this is how the algorithm iterates
#       [ [1/3, 1/2] ]
#       [ [1/3, 2/5, 1/2] ]
#       [ [1/3, 3/8, 2/5, 3/7, 1/2] ] --> [ [1/3], [2/5, 3/7, 1/2] ] 
#       [ [1/3], [2/5, 5/12, 3/7, 4/9, 1/2] ] --> [ [1/3], [2/5], [3/7], [1/2] ]
#   ans: [2/5, 3/7]
# so once we reach a fraction with a denominator that is too large, we remove it and split the interval
# we iterate until we only have intervals of length 1
# the number of singular intervals - 2 (for the endpoints)
#
# This is about the same speed as the brute force method above
def constructive(N, f1, f2):

    fractions = []                      # storing final result
    intervals = [ [f1, f2] ]            # data structure we are iterative over

    while len(intervals) != 0:
        updated_intervals = []
        
        # iterate over each interval
        for I in intervals:
            if len(I) == 1:
                fractions.append(I[0])
                continue
            
            updated_I = [I[0]]
            for i in range(len(I)-1):
                # for each pair of fractions in the interval I
                left, right = I[i], I[i+1]
                # calculate the funny-addition between them to get the next fraction
                f = funny_addition(left, right)
                # If the fraction is too large, we disregard it and split the interval
                if f[1] > N:
                    updated_intervals.append( updated_I )
                    updated_I = [right]
                else:
                    # otherwise, we add the new fraction to continue iterating
                    updated_I.append(f)
                    updated_I.append(right)

            updated_intervals.append(updated_I)
        intervals = updated_intervals
    
    #fractions = list(sorted(fractions, key=lambda f: f[0]/f[1]))
    #print(fractions)
    return len(fractions) - 2

def main(N=12000, f1=(1, 3), f2=(1, 2)):
    n1, d1 = f1
    n2, d2 = f2

    #total = brute_force(N, f1, f2)
    total = constructive(N, f1, f2)

    print(f"The number of reduced proper fractions with d <= {N} between {n1}/{d1} and {n2}/{d2} is:", total)
    return total


if __name__ == "__main__":
    main()
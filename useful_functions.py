def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    prime_list = [  2,   3,   5,   7,   11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
                    3,   59,  61,  67,  71,  73,  79,  83,  89,  97,  101, 103, 107, 109, 113,
                    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in prime_list:
        return True
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def Sieve_of_Eratosthenes(n):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError("must be integer")
    if n < 2:
        raise ValueError("must be greater than one")
    m = (n-1) // 2 #list only needs to be half as long bc we dont care about even numbers
    sieve = [True] * m
    i = 0
    p = 3
    prime_list = [2] #add 2 as the exception
    #this while loop is equivilent to the while loop in the first Sieve function
    #it just looks different because the parameters are different
    while p*p < n:
        #if the number hasnt been crossed out we add it
        if sieve[i]:
            prime_list += [p]
            #j is the multiples of p
            j = 2*i*i + 6*i + 3 #j = (p^2-3)/2 where p = 2i+3 (see below comments)
            #this is equivilent to the for loop in the previous Sieve fuction
            while j < m:
                sieve[j] = False
                j += 2*i + 3 #p = 2i+3
        i += 1
        p += 2
        #this is where the p = 2i+3
        #p starts at 3 and is upped by 3, where i starts at 0 and is upped by 1
    #this while loop then adds the remaining primes to the prime list
    while i < m:
        if sieve[i]:
            prime_list += [p]
        i += 1
        p += 2
    return prime_list


# integer factorization by Trial Division
def Prime_Factors(n):
    # Error Check
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        return []
    factors = []
    # as always, take care of the 2s first bc they are easy
    while n % 2 == 0:
        factors += [2]
        n =  n // 2
    # if n was purely a power of 2, then the function ends here
    if n == 1:
        return factors
    # since we got rid of the 2's potential factors, f can start at 3
    # other than that, this loop is pretty self explainitory
    f = 3
    while f*f <= n:
        if n % f == 0:
            factors += [f]
            n = n // f
        else:
            f += 2
    return factors + [n]


# got this from https://www.rookieslab.com/posts/most-efficient-way-to-find-all-factors-of-a-number-python-cpp
def get_factors(n):
    result = set([])
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return result

from functools import reduce

# got this from stack exchange, basically just a one-liner for the above
# not sure what is more efficient
def get_factors_compressed(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factorial_iteration(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def factorial_recursion(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * factorial(n-1)

def factorial_list(n):
    out = [1]
    f = 1
    for i in range(1, n+1):
        f *= i
        out += [f]
    return out

def first_factorials(n):
    F = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return F[n]

from itertools import chain

def powerset(L, include_self=True):
    n = len(L)
    if include_self:
        n += 1
    return chain.from_iterable(combinations(L, r) for r in range(n))

def allFactors(n):
    prime_factors = Prime_Factors(n)
    f = set()
    for subset in powerset(prime_factors, include_self=False):
        f.add(math.prod(subset))
    return f

def getDigits(n):
    return [int(d) for d in str(n)]

def numDigits(n):
    return len(str(n))

def numberify(digits):
    return int( "".join([str(d) for d in digits]) )

def reverse_int(n):
    return int( "".join(reversed(str(n))) )

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)

def gcd_iterative(a, b):
    if b > a:
        a, b = b, a

    # gcd(a, b) = gcd(b, a%b)
    while b != 0:
        a, b = b, a%b
    return a

def reduce_fraction(numerator, denominator):
    k = gcd(numerator, denominator)
    return numerator // k, denominator // k

def modular_exponentiation(b, e, m):
    b = b % m
    if b == 0:
        return 0
    
    ans = 1         # = b^e mod m
    while e > 0:
        # If e is odd, multiply n with result
        if e % 2 == 1:
            ans = (ans * b) % m
 
        # e must be even now
        e = e // 2
        b = (b * b) % m
    
    return ans

from collections import defaultdict
D = defaultdict(list)

# This is the most numerically stable way to write this function
# If you try to do something like 
#   return int(math.sqrt(n)) == math.sqrt(n)
# you can run into problems where the sqrt function doesn't have enough precision
def isPerfectSquare(n):
    s = math.sqrt(n)
    return math.floor(s)**2 == n or math.floor(s)**2 == n

def N_forloops(N_values):
    N_values = [list(values) for values in N_values]

    # The data structure to simulate the N forloops
    loop_indexes = [0] * len(N_values)
    index_length = [len(values)-1 for values in N_values]
    loop_values = [values[i] for i, values in zip(loop_indexes, N_values)]
    
    # The print statements represent processing the current state of the forloop
    print(loop_indexes, '\t', loop_values)
    
    # i represents the nest level of the for loop
    # i = 0 is the inner-most nested loop
    i = 0
    while i < len(N_values):
        if loop_indexes[i] >= index_length[i]:
            loop_indexes[i] = 0
            i += 1
            continue

        loop_indexes[i] += 1
        for k in range(i+1):
            #loop_values[k] = loop_values[i]                # use this in the case where you don't want repeats
            loop_values[k] = N_values[k][loop_indexes[k]]
        i = 0
        print(loop_indexes, '\t', loop_values)


# See P042.py for the math behind this
def Triangle(n):
    return (n*(n+1)) // 2
def isTriangle(x):
    n = (-1 + math.sqrt(8*x+1))/2
    return x == Triangle(math.floor(n)) or x == Triangle(math.ceil(n))


# See P044.py for the math behind this
def Pentagon(n):
    return (n*(3*n-1)) // 2
def isPentagon(x):
    n = (1 + math.sqrt(24*x + 1)) / 6
    return x == Pentagon(math.floor(n)) or x == Pentagon(math.ceil(n))


# See P045.py for the math behind this
def Hexagon(n):
    return n*(2*n-1)
def isHexagon(x):
    n = (1 + math.sqrt(8*x + 1)) / 4
    return x == Hexagon(math.floor(n)) or x == Hexagon(math.ceil(n))


# computes d digits of a/b
def division_by_hand(a, b, d):
    if int(a) != a:
        raise TypeError(f"Got input a={a}, but expected an integer")
    if int(b) != b:
        raise TypeError(f"Got input b={b}, but expected an integer")
    if int(d) != d:
        raise TypeError(f"Got input d={d}, but expected an integer")
    if d <= 0:
        raise ValueError(f"Got input d={d}, but expected a positive integer")

    if a == 0:
        return f"{0}.{'0'*(d-1)}"
    if b == 0:
        raise ValueError("Cannot divide by 0")

    negative = ((a < 0) != (b < 0))
    dividend = abs(a)
    divisor  = abs(b)

    # doing the division algorithm we all know
    digits = [dividend // divisor]
    remainder = dividend % divisor
    while len(str(digits[0])) + len(digits[1:]) < d:

        remainder *= 10
        digits.append(remainder // divisor)
        remainder %= divisor
    
    # putting output into a nice form
    quotent_str = f"{digits[0]}.{''.join([str(x) for x in digits[1:]])}"
    if negative:
        quotent_str = "-" + quotent_str
    return quotent_str


# How does this work
#   We can decompose sqrt(n) as:        sqrt(n) = 10*A + B
#   Therefore                           n = (10*A + B)^2 = 100*A^2 + 20AB + B^2
#   
#   We can update our approximation of sqrt(n) by finding the largest B we can add
def sqrt_by_hand(n, d):
    if int(n) != n:
        raise TypeError(f"Got input n={n}, but expected an integer")
    if int(d) != d:
        raise TypeError(f"Got input d={d}, but expected an integer")
    if d <= 0:
        raise ValueError(f"Got input d={d}, but expected a positive integer")

    if n == 0:
        return f"{0}.{'0'*(d-1)}"
    negative = (n < 0)
    n = abs(n)
    
    # putting n in a more usable form
    digits = [int(d) for d in str(n) if d != '.']
    if len(digits) % 2 == 1:
        digits = [0] + digits
    
    sqrt = 0
    remainder = 0

    while len(str(sqrt)) < d:

        # bring down next two digits
        remainder = 100*remainder + 10*digits[0] + digits[1]

        # adding zeros to end of number for next iterations
        digits = digits[2:] + [0, 0]

        # finding largest B s.t. 20*A*B + B^2 <= remainder
        B = 0
        while 20*sqrt*B + B**2 <= remainder:
            B += 1
        B -= 1

        # y is what goes under the number that was brought down
        y = 20*sqrt*B + B**2

        # update the remainder
        remainder -= y

        # x is the next digit in the sqrt
        sqrt = 10*sqrt + B
    
    # Putting output into a nice form

    # I felt like this way was kinda cheating
    """
    import math
    non_decimal_part = str(int(math.sqrt(n)))
    sqrt_str = str(sqrt)
    sqrt_str = sqrt_str[:len(non_decimal_part)] + '.' + sqrt_str[len(non_decimal_part):]
    """

    # Fun fact: the number of digits in the sqare root of a number is n//2
    # So we can use this to figure out where the decimal goes instead
    non_decimal_length = (len(str(int(n)))+1) // 2
    sqrt_str = str(sqrt)
    sqrt_str = sqrt_str[:non_decimal_length] + '.' + sqrt_str[non_decimal_length:]
    
    if negative:
        sqrt_str += " i"
    return sqrt_str

if __name__ == "__main__":
    #for n in range(-10, 1001):
    #    print( sqrt_by_hand(n, 10) )
    for n in range(1, 20):
        print( division_by_hand(1, n, 20) )
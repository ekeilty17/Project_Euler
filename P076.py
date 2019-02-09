# Using Euler's Formala for partitials:
#   SUM{ P(n) * x**n } = PRODUCT{ 1/(1 - x**n) } = PRODUCT{ 1 + x**n  +  x**(2n) + ...) }
#
# So if we multiply enough of the RHS out, then we can get the coefficients on the LHS
# and that will give us the number of partitions

class Term:    
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
    
    def __str__(self):
        if self.coef == 0:
            return ""
        if self.exp == 0:
            return str(self.coef)
        if self.coef == 1 and self.exp == 1:
            return "x"
        if self.coef == 1:
            return "x^" + str(self.exp)
        if self.exp == 1:
            return str(self.coef) + "x"
        return str(self.coef) + "x^" + str(self.exp)

    def copy(self):
        return Term(self.coef, self.exp)
    
    def add(self, term):
        if self.exp == term.exp:
            self.coef += term.coef

    def multiply(self, term):
        self.coef *= term.coef
        self.exp += term.exp


class Polynomial:
    def __init__(self, terms=[]):
        self.terms = terms
        self.terms.sort(key=lambda x: -x.exp)

    def __str__(self):
        out = ""
        for i in range(0, len(self.terms)):
            if i != 0:
                out += " + "
            out += str(self.terms[i])
        return out

    def copy(self):
        P = Polynomial([])
        for t in self.terms:
            P.terms += [t.copy()]
        P.terms.sort(key=lambda x: -x.exp)
        return P

    def add_term(self, term):
        for t in self.terms:
            if t.exp == term.exp:
                t.add(term)
                return None
        self.terms += [term.copy()]
        self.terms.sort(key=lambda x: -x.exp)

    def __add__(self, poly):
        P = self.copy()
        for t in poly.terms:
            P.add_term(t)
        return P
    
    def __mul__(self, poly):
        out = Polynomial([])
        for t1 in self.terms:
            for t2 in poly.terms:
                out.add_term(Term(t1.coef*t2.coef, t1.exp+t2.exp))
        return out

"""
x0 = Term(3, 0)
x1 = Term(1, 1)
P1 = Polynomial([x0, x1])

y0 = Term(2, 0)
y1 = Term(1, 1)
P2 = Polynomial([y0, y1])

print P1
print P2
print
print P1 + P2
print
print P1 * P2
"""

# This will actually calculate the number of distinct partitions
# which menas you can't use repeated numbers in the partition
# by Euler's theorem, this is also equal to the number of odd partitions
# This utilizes te formula
#   SUM{ D(n) * x**n } = SUM{ O(n) * x**n } = PRODUCT{ 1 + x**n }
def DistinctPartitions(n)
    # starting with polynomial x + 1
    P = Polynomial([Term(1, 1), Term(1, 0)])
    for i in range(2, n+1):
        print P
        P *= Polynomial([Term(1, i), Term(1, 0)])
        P.terms = list(filter(lambda x: x.exp <= n, P.terms))

    return P.terms[0].coef

# starting with polynomial P = 1
def Partition(n):
    if n == 0 or n == 1:
        return 1
    P = Polynomial([Term(1, 0)])
    for k in range(1, n+1):
        # generating polynomial to multiply
        # Q = 1 + x^e + x^(2*e) + ... + x^(k*e) + ... s.t. k*e <= n
        Q = Polynomial([])
        for e in range(0, n/k+1):
            Q.add_term(Term(1, k*e))
        P *= Q
        P.terms = list(filter(lambda x: x.exp <= n, P.terms))

    return P.terms[0].coef

n = 100
p = Partition(n)
# Note: Euler's formula includes n as a valid partition
#   for example: P(4) = {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}, {4}
# However, the problem does not consider {4} a valid partition, so we need to subtract 1
print "number of partitions of", n, "is", p-1

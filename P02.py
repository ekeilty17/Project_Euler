"""
def fibo(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
"""

#recursion probably isnt the answer since the numbers are getting really high
#I think I should be summing while I generate new numberes

fibo = [1, 1]
accum = 0
while fibo[1] < 4000000:
    #checking if it's even
    if fibo[1] % 2 == 0:
        accum += fibo[1]
    #getting next fibonacci number
    temp = fibo[1]
    fibo[1] = fibo[0] + fibo[1]
    fibo[0] = temp

print accum

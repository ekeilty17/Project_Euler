def numDigit(n):
    cnt = 0
    while n != 0:
        n /= 10
        cnt += 1
    return cnt

def get_nth_digit(N,n):
    for i in range(0,n-1):
        N /= 10
    return N%10 

def fract(n):
    if n == 0:
        return 0
    num = 1
    dec_place = 1
    while dec_place < n:
        #print num,dec_place
        num += 1
        dec_place += numDigit(num)
    #print "\t",dec_place,n
    return get_nth_digit(num,dec_place - n + 1)

print fract(1)*fract(10)*fract(100)*fract(1000)*fract(10000)*fract(100000)*fract(1000000)

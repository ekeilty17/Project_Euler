#all the usual bit operations work in python
"""
b = 0b10000000
for i in range(0,10):
    print bin(b >> i)

x = 0b10
y = 0b11
print bin(x),bin(y)
print "~",bin(~x),bin(~y)
print "&",bin(x & y)
print "|",bin(x | y)
print "^",bin(x ^ y)
"""

"""
#get ascii of a character
print bin(ord('b'))
print bin(ord('B'))

#get character from ascii
print chr(0b1100010)        #97
print chr(0b1000010)        #122

for i in range(32,123):
    print i,chr(i)
"""

def isEnglishChar(c):
    if 32 <= c <= 122:
        return True
    return False

def decrypt(s, key):
    #in this particular instance I can skip the converting the string into ascii
    out = ''
    for i in range(0,len(s),len(key)):
        for j in range(0,len(key)):
            if i+j < len(s):
                out += chr( int(s[i+j]) ^ ord(key[j]) )
                #out += chr(bin(ord(s[i+j])) ^ bin(ord(key[j])))
    return out

#get lines of a textfile
lines = open('p059_cipher.txt','r').readlines();
lines = lines[0].strip().split(',')     #strip gets rid of the \n at the end
#print lines

#convert to binary list
bin_lines = [int(x) for x in lines]
#print bin_lines

#searching for the encryption key
possible_first = range(97,123)
possible_second = range(97,123)
possible_third = range(97,123)

#for a letter to be an encrption key, xoring it should produce an english character for every letter in its period

#eliminating possible characters for first letter in key
for c in range(97,123):
    for b in range(0,len(bin_lines),3):
        if not isEnglishChar(bin_lines[b] ^ c):
            possible_first.remove(c)
            break

#eliminating possible characters for second letter in key
for c in range(97,123):
    for b in range(1,len(bin_lines),3):
        if not isEnglishChar(bin_lines[b] ^ c):
            possible_second.remove(c)
            break

#eliminating possible characters for third letter in key
for c in range(97,123):
    for b in range(2,len(bin_lines),3):
        if not isEnglishChar(bin_lines[b] ^ c):
            possible_third.remove(c)
            break

print possible_first
print possible_second
print possible_third

#making all possible combinations of possible encryton keys
possible_keys = []
for f in possible_first:
    for s in possible_second:
        for t in possible_third:
            possible_keys += [chr(f) + chr(s) + chr(t)]

print possible_keys

for k in possible_keys:
    print decrypt(lines,k)
    print

print possible_keys[-1]
print

#getting sum of ascii values of original text
original = decrypt(lines,possible_keys[-1])
accum = 0
for c in original:
    accum += ord(c)
print accum

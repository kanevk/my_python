__author__ = 'Sanal'
__link__ = 'https://www.hackerrank.com/contests/w10/challenges/cipher'

# Jack and Daniel are friends.
# They want to encrypt their conversation so that they can save themselves from interception by a detective agency. So they invent a new cipher.
# Every message is encoded to its binary representation B of length N.
# If B=1001010 and K=4 it looks so:
#


def xor(s):
    x=0
    for i in s:
        x=x^int(i)
    return x


num = raw_input().split(' ')
l = int(num[0])
k = int(num[1])
n = raw_input()

x='0'*(k-2)+n[0]
for i in range(1,l):
    x = x + str(xor(x[i-1:]+n[i]))
print x[k-2:]




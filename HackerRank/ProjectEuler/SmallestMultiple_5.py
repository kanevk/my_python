__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'



def multis(n):
    i = 1
    while True:
        x = [i%j==0 for j in range(2,n+1)]
        if all(x):
            return i
        i=i+1
    return -1

for i in range(input()):
    print multis(input())
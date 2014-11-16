__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'


def high(n):
    if n<=1:
        return 1
    else:
        return n+high(n-1)


for i in range(input()):
    print high(input()-1)
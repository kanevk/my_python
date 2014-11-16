__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'



def combinations(x,n):
    print x,n
    if n<0:
        return False
    if n==0:
        print '*'
        return True
    for i in x:
        if n>0:
            combinations(x,n-i)

print combinations([5, 5, 15, 10],15)
__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'

def collatz(n,l):
    if n==1:
        return l+1
    if n%2==0:
        n = n/2
    else:
        n = 3*n + 1
    return collatz(n,l+1)




x= [collatz(i,0) for i in range(1,21)]
print x
print ''.join([str(k) for k in x]).rfind(str(max(x)))
print ''.join([str(k) for k in x])
print max(x)
print  x.index(max(x))+1
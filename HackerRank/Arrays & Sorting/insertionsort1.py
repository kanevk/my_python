__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'
__link__ = 'https://www.hackerrank.com/challenges/insertionsort1'
n= input()
x = [int(i) for i in raw_input().split(' ')]
last = x[len(x)-1]
for i in range(len(x)-2,-1,-1):
    if last<x[i]:
        x[i+1] = x[i]
    else:
        x[i+1] = last
    for i in x:
        print i,
    print ''

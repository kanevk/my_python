__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'
__link__ = 'https://www.hackerrank.com/challenges/angry-children'

n = input()
k = input()
s=[]
for i in range(n):
    s.append(input())

s.sort()
print max(s[:k])-min(s[:k])
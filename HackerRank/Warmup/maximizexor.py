__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'
__link__ ='https://www.hackerrank.com/challenges/maximizing-xor'
#
# Given two integers: L and R,
#
# find the maximal values of A xor B given, L <= A <= B <= R
#
# Input Format
# The input contains two lines, L is present in the first line.
# R in the second line.
l=input()
r=input()
max = 0
for i in range(l,r+1):
    for j in range(l,r+1):
        if i^j>max:
            max = i^j
print max
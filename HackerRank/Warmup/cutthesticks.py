__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'
__link__ = 'https://www.hackerrank.com/challenges/cut-the-sticks'

# You are given N sticks, where each stick is of positive integral length. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.
#
# Suppose we have 6 sticks of length
#
# 5 4 4 2 2 8
# then in one cut operation we make a cut of length 2 from each of the 6 sticks. For next cut operation 4 sticks are left (of non-zero length), whose length are
#
# 3 2 2 6
# Above step is repeated till no sticks are left.
#
# Given length of N sticks, print the number of sticks that are cut in subsequent cut operations.

n = input()
no = raw_input().split()
x = [int(i) for i in no]

def mini(x):
    m =9999
    for i in x:
        if i<m and i!=0:
            m=i
    return m

def deduct(x,m):
    y=[]
    for i in x:
        if i!=0:
            y.append(i-m)
        else:
            y.append(0)
    return y

def countOnes(x):
    s=0
    for i in x:
        if i!=0:
            s=s+1
    return s

while not all(i==0 for i in x):
    m = mini(x)
    print countOnes(x)
    x = deduct(x,m)

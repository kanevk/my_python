__author__ = 'Sanal'
__link__ = 'https://www.hackerrank.com/challenges/sherlock-and-squares'


#Sherlock and Squares
# Watson gives two integers A & B to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).
#
# A square integer is an integer which is the square of any integer. For example, 1, 4, 9, 16 are some of the square integers as they are squares of 1, 2, 3, 4 respectively.
#
# Input Format
# First line contains T, the number of testcases. T test cases follow, each in a newline.
# Each testcase contains two space separated integers denoting A and B.
#
# Output Format
# For each testcase, print the required answer in a new line.
import math



for i in range(input()):
    no = raw_input().split(' ')
    a = int(no[0])
    b = int(no[1])


    nearA = (int(math.sqrt(a)))
    nearB = (int(math.sqrt(b))+1)

    count = 0
    for i in range(nearA,nearB+1):
        if i*i>=a and i*i<=b:
            count = count +1
    print count
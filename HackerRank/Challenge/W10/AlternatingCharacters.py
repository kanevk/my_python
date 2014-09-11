__author__ = 'Sanal'
__link__ = 'https://www.hackerrank.com/contests/w10/challenges/alternating-characters'

# Alternating Characters
# Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.
#
# Your task is to find the minimum number of required deletions.
#
# Input Format
# The first line contains an integer T i.e. the number of test cases.
# Next T lines contain a string each.
#
# Output Format
# Print minimum number of required steps for each test case.


def altercheck(s):
    l = len(s)
    a_s = s.count('A')
    b_s = s.count('B')

    if l==a_s:
        return a_s-1
    if l==b_s:
        return b_s-1
    ab_s = s.count('AB')
    ba_s = s.count('BA')
    return l - ab_s-ba_s -1

for i in range(input()):
    print altercheck(raw_input())


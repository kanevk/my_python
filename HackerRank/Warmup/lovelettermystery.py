__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'
__link__ = 'https://www.hackerrank.com/challenges/the-love-letter-mystery'

#The Love-Letter Mystery
# James got hold of a love letter that his friend Harry has written for his girlfriend. Being the prankster that James is, he decides to meddle with it. He changes all the words in the letter into palindromes.
#
# While modifying the letters of the word, he follows 2 rules:
#
# (a) He always reduces the value of a letter, e.g. he changes 'd' to 'c', but he does not change 'c' to 'd'.
# (b) If he has to repeatedly reduce the value of a letter, he can do it until the letter becomes 'a'. Once a letter has been changed to 'a', it can no longer be changed.
#
# Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations he carries out to convert a given string into a palindrome.
#
#
# Input Format
# The first line contains an integer T, i.e., the number of test cases.
# The next T lines will contain a string each.
#
# Output Format
# A single line containing the number of minimum operations corresponding to each test case.
#
# All characters are lower cased english letters.

def isPalin(s):
    return s==s[::-1]

for k in range(input()):
    s = raw_input()
    count = 0
    for i in range(len(s)-1,-1,-1):
        if not isPalin(s):
            count = count + abs(ord(s[i])-ord(s[len(s)-i-1]))
            s= s[:i]+s[len(s)-i-1]+s[i+1:]
        else:
            break
    print count
__author__ = 'Sanal'
__link__ = 'https://www.hackerrank.com/contests/w10/challenges/cipher'
# One day John had to take care of his little nephew Jim. He was very busy, so he gave Jim a big bag full of building bricks. The bricks are of various heights: at most 15 different heights. For each height, the bag contains infinitely many bricks.
#
# Jim is good at building towers and can build one tower in exactly 2 minutes, regardless of its height. John wants to know the time Jim requires to build all possible towers.
#
# Input Format
# There are 3 lines of input. First line contains an integer, N, the height of tower to be built. Second line contains another integer, K, which represents different heights of bricks available in the bag. Third line contains K distinct integers representing the available heights.
#
# Output Format
# In one line print the number of minutes Jim requires to build all possible towers. As this number can be very large, print the number modulo



n=10
x = [2,3]
s = []
while(len(x)!=0):
    mx = max(x)
    no = n/mx
    for i in range(no):
        s.append(mx)
    n=n%mx
    x.remove(mx)

print s

__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'
__link__ = 'https://www.hackerrank.com/categories/algorithms/arrays-and-sorting/challenges/page/1'

a = raw_input()
b = raw_input()


# a='abc'
# b='cde'

a1={}
b1={}


for i in a:
    if i in a1:
        a1[i] = a1[i] + 1
    else:
        a1[i] = 1

for i in b:
    if i in b1:
        b1[i] = b1[i] + 1
    else:
        b1[i] = 1

s = 0
for i in range(97,123):
    x = 0
    y = 0
    if chr(i) in a1:
        x = a1[chr(i)]
    if chr(i) in b1:
        y = b1[chr(i)]
    # s = s + max(x,y) - min(x,y)
    s = s + abs(x-y)
print s
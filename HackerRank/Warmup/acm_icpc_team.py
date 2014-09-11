__author__ = 'Sanal'
__link__   = 'https://www.hackerrank.com/challenges/acm-icpc-team'

#
# You are given a list of N people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not. Find out the maximum number of topics a 2-people team can know. And also find out how many teams can know that maximum number of topics?
#
# Input Format
#
# The first line contains two integers N and M separated by a single space, where N represents the number of people, and M represents the number of topics. N lines follow.
# Each line contains a binary string of length M. In this string, 1 indicates that the ith person knows a particular topic, and 0 indicates that the ith person does not know the topic.
#
# Output Format
#
# On the first line, print the maximum number of topics a 2-people team can know.
# On the second line, print the number of teams that can know the maximum number of topics.
#
x=[]
nums = raw_input().split()
n = int(nums[0])
m = int(nums[1])
for i in range(n):
    x.append(int(raw_input(),2))

a = []
b = []
max=0
for i in x:
    for j in x:
        if i!=j and [i,j] not in a:
            a.append([i,j])
            a.append([j,i])
            cnt = str(bin(i + j)).count('1')
            b.append(cnt)
print b,type(b)

print max(b)
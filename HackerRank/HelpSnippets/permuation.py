__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'


def permute(s,i):
    if i==len(s)-1:
        print s
    else:
        for j in range(i,len(s)):
            s[i],s[j]=s[j],s[i]
            permute(s,i+1)
            s[i],s[j] = s[j],s[i]


permute(list('abc'),0)
__author__ = 'san'
__hacker_rank = 'https://www.hackerrank.com/sanaltsk'


def combinations(string):
     yield ''
     for i, d in enumerate(string):
             for comb in combinations(string[i+1:]):
                     yield d + comb


print [comb for comb in combinations('sanal')]
__author__ = 'Sanal'
from itertools import permutations
perms = [''.join(p) for p in permutations('5554')]
print perms

#unique permutation
s  = set(perms)
print s

from itertools import combinations
combi = [x for x in combinations('ab',2)]
print combi

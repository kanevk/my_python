__author__ = 'Sanal'
import itertools
print map(''.join, itertools.product('ab',repeat=3))
# ['aa', 'ab', 'ba', 'bb']

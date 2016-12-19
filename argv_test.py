# Freddy/Fangyu@BNU
# 12/19/2016


import sys
import os

args = sys.argv

print(args)

print(sys.argv[1:])

for arg in args:
	print(arg)

'''Output'''
'''
(py3env1) ❯ python argv_test.py 1 2 3 4
['argv_test.py', '1', '2', '3', '4']
['1', '2', '3', '4']
argv_test.py
1
2
3
4
'''
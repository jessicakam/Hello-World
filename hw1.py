#!/usr/bin/env python
import sys

def main():
	'''
	4/2/15
	my attempt at solving Jess's hw assignment
	# This function returns the smaller number of the two inputs
	# Inputs:
	#   a: the first number to compare
	#   b: the second number to compare
	#
	# Output:
	#   answer: the smaller number of a and b
	
	revisited 4/3/15 and modified
	'''
	a = 3
	b = 3
	c = 3
	
	answer = min(a,b,c)
	print answer

def min(a, b, c):
	answer = 0

	if a < b and b < c:
		answer = a
    
	elif c < b and b < c:
		answer = c
	else:
		answer = b
	return answer
'''
if __name__ == '__main__':
	main()
'''
'''
a = [7, 8, 9, 10]
limit = len(a) - 1

print a[0]

while len(a[0]) < limit:
	a[0] = a[0] + 1
	#also equivalent to a += 1
	print a[0]

'''
'''
a = [7, 8, 9, 10]
first_position = 0
limit = len(a) - 1

while first_position < limit:
	print a[first_position]
	first_position = 0
	print "fp" + str(first_position)

print a[first_position]
'''

list = [5, 6, 7, 8, 9]
'''
for item in list:
	print item
'''

for index, item in enumerate(list):
	print str(index) + "," + str(item)









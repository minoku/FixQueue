#! /usr/bin/python

import FixQueue

if __name__ == "__main__" :
	fq = FixQueue(2) # 2 means queue size

	fq.append('a')
	fq.append('b')

	print (fq) # ['a', 'b']

	fq.append('c')

	print (fq) # ['b', 'c']

	print (fq.pop()) # b

	print (fq) # ['b']


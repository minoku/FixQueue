========
FixQueue
========

Simplest Queue module to make a fixed size queue on your platform and apps.

You just need to use FixQueue-based queues.


=======
Install
=======
pip install fixqueue


=============
Basic Example
=============
	from FixQueue import FixQueue

	if __name__ == "__main__" :
		fq = FixQueue(2) # 2 means queue size
	
		fq.append('a')
		fq.append('b')
	
		print (fq) # ['a', 'b']
	
		fq.append('c')
	
		print (fq) # ['b', 'c']
	
		print (fq.pop()) # b
	
		print (fq) # ['b']



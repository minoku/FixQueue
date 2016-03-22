
class FixQueue(list) :

	def __init__(self, queue_size) :
		self.queue_size = queue_size

		print ("Initializing - FixQueue (Queue Size : %s) " % (self.queue_size))

	def append(self, data) :
		list.append(self, data)

		if len(self) > self.queue_size : del self[0]

	def clear(self) :
		del self[:]

	def pop(self, index=0) :
		rvalue = self[index]
		del self[index]
		return rvalue
 

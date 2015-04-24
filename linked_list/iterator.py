class Iterator:
	def __init__(self,current):
		self.current = current
	def getNext(self):
		if self.hasNext():
			self.current = self.current.next
		return self.current
	def hasNext(self):
		if self.current.next:
			return True
		return False
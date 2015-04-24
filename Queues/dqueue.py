class Queue:
	def __init__(self):
		self.items = {}
		self.min = 0
		self.max = 0

	def isEmpty(self):
		return self.items == {}

	def enqueue(self, item):
		self.items[self.max] = item
		self.max += 1

	def dequeue(self):
		item = self.items[self.min]
		del self.items[self.min]
		self.min += 1
		return item

	def size(self):
		return self.max - self.min





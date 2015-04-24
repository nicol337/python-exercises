from node import Node

class OrderedList:
	def __init__(self):
		self.head = None

	def add(self, item):
		new_node = Node(item)
		new_node.setNext(self.head)
		self.head = new_node

	def remove(self, item):
		

	def search(self, item):
		curr = self.head
		while curr != None:
			if curr.getData() == item:
				return True
			curr = curr.getNext()
		return False

	def isEmpty(self):
		return self.head == None

	def size(self):
		count = 0
		while curr != None:
			curr = curr.getNext()
			count += 1
		return count

	def index(self, item):
		count = 0
		curr = self.head
		while curr != None:
			if curr.getData() == item:
				return count
			curr = curr.getNext()
			count += 1
		return -1
		

	def pop(self, index=None):
		pass

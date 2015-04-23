from node import Node

class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		new_node = Node(item)
		new_node.setNext(self.head)
		self.head = new_node

	def size(self):
		current_node = self.head
		length = 0
		while current_node != None:
			length += 1
			current_node = current_node.getNext()
		return length

	def search(self, item):
		current_node = self.head
		while current_node != None:
			if current_node.data == item:
				return True
			current_node = current_node.getNext()
		return False
	

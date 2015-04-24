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
			if current_node.getData() == item:
				return True
			current_node = current_node.getNext()
		return False

	def remove(self,item):
		current_node = self.head
		previous_node = None
		while current_node != None:
			if current_node.getData() == item:
				if previous_node == None:
					self.head = None
				else:
					previous_node.setNext(current_node.getNext())
				return True
			previous_node = current_node
			current_node = current_node.getNext()
		return False

	def append(self, item):
		current_node = self.head
		previous_node = None
		if self.head == None:
			self.head = Node(item)
			return
		while current_node != None:
			previous_node = current_node
			current_node = current_node.getNext()
		previous_node.setNext(Node(item))
	
	def pop(self, index=None):
		current_node = self.head
		previous_node = None
		if index == None:
			while current_node.getNext() != None:
				previous_node = current_node
				current_node = current_node.getNext()
			if previous_node == None:
				item = self.head.getData()
				self.head = None
			else:
				item = current_node.getData()
				previous_node.setNext(None)
			return item
		else:
			itr = 0
			while current_node.getNext() != None and itr != index:
				previous_node = current_node
				current_node = current_node.getNext()
				itr += 1
			if itr+1 < index:
				return None
			else:
				item = current_node.getData()
				if previous_node == None:
					self.head = current_node.getNext()
				else:
					previous_node.setNext(current_node.getNext())
				return item

	def insert(self, index, item):
		itr = 0
		current_node = self.head
		previous_node = None
		new_node = Node(item)
		# if index == 0:
		# 	new_node.setNext(self.head)
		# 	self.head = new_node
		# 	return
		while itr < index and current_node.getNext() != None:
			previous_node = current_node
			current_node = current_node.getNext()
			itr += 1
		if itr == index:
			if previous_node == None:
				new_node.setNext(self.head)
				self.head = new_node
			else:
				new_node.setNext(current_node)
				previous_node.setNext(new_node)

	def index(self, item):
		itr = 0
		current_node = self.head
		while current_node != None and current_node.getData() != item:

			current_node = current_node.getNext()
			itr += 1
		place = -1 if current_node == None else itr
		return place



		


	

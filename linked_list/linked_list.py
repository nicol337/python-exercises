from node import Node
from iterator import Iterator

class LinkedList:
	def __init__(self,head=None):
		self.head = head
	def insert(new_node, index=False):
		if not index:
			iterator = Iterator(self.head)
			while iterator.hasNext():
				iterator.getNext()
			iterator.next = new_node
		else:
			counter = 0
			iterator = iterator(self.head)
			while iterator.hasNext() and counter < index:
				iterator.get
				counter+=1
			if counter < index:
				self.insert(new_node)
	def __str__(self):
		str = ""
		iterator = Iterator(self.head)
		while iterator.hasNext():
			str+=iterator.getNext()+"->"
		str+="NONE"
		return str

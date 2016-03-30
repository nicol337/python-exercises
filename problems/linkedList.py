import random

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, item):
		curr = self.head
		newNode = Node(item)
		if curr == None:
			self.head = newNode
		else:
			while curr.next != None:
				curr = curr.next
			curr.next = newNode

	def pop(self):
		curr = self.head
		if curr == None:
			return None
		else:
			prev = None
			while curr.next != None:
				prev = curr
				curr = curr.next
			if prev != None:
				prev.next = None
			else:
				self.head = None
			return curr.data

	def sortedInsert(self, item):
		curr = self.head
		newNode = Node(item)
		if curr == None:
			self.head = newNode
		else:
			prev = None
			while curr != None and curr.data < item:
				prev = curr
				curr = curr.next
			if prev != None:
				prev.next = newNode
				newNode.next = curr
			else:
				newNode.next = curr
				self.head = newNode

	def insert(self,item,index):
		curr = self.head
		newNode = Node(item)
		if (curr == None and index == 0) or (index == 0):
			self.head = newNode
			newNode.next = curr
		else:
			itr = 0
			prev = None
			while curr != None and itr < index:
				prev = curr
				curr = curr.next
				itr += 1
			if itr == index:
				prev.next = newNode
				newNode.next = curr
			else:
				return

	



	def __str__(self):
		curr = self.head
		string = ''
		while curr != None:
			string += str(curr.data) + ' '
			curr = curr.next
		return string[:-1]


def test1():
	linkedList = LinkedList()
	for i in range(10):
		linkedList.push(i)
		print(linkedList)
	for i in range(10):
		linkedList.pop()
		print(linkedList)

def findLoop(linkedList):
	itr1,itr2 = linkedList.head,linkedList.head.next
	ctr = 0
	while itr1 != itr2:
		ctr += 1
		itr1 = itr1.next
		itr2 = itr2.next.next
	print(ctr)
	print(itr1,itr2)

def test2():
	linkedList = LinkedList()
	
	for i in range(10):
		linkedList.push(i)
	loopStart = linkedList.head
	for i in range(3):
		loopStart = loopStart.next
	itr = linkedList.head
	while itr.next != None:
		itr = itr.next
	itr.next = loopStart

	findLoop(linkedList)

	

def reverseList(linkedList):
	curr = linkedList.head
	if curr != None:
		prev = curr
		curr = curr.next
		while curr != None:
			prev.next = curr.next
			curr.next = linkedList.head
			linkedList.head = curr
			curr = prev.next


def test3():
	linkedList = LinkedList()
	for i in range(0):
		linkedList.push(i)
	reverseList(linkedList)
	print(linkedList)




def test4():
	linkedList = LinkedList()
	for i in range(10):
		item = random.randint(1,50)
		linkedList.sortedInsert(item)
		print(linkedList)

def test5():
	linkedList = LinkedList()
	for i in range(10):
		linkedList.push(i)
	print(linkedList)
	linkedList.insert('a',11)
	print(linkedList)
	linkedList.insert('b',5)
	print(linkedList)
	linkedList.insert('c',5)
	print(linkedList)
	linkedList.insert('d',0)
	print(linkedList)
	linkedList.insert('e',1)
	print(linkedList)



def main():
	# test1()
	# test2()
	# test3()
	# test4()
	test5()	

	


main()
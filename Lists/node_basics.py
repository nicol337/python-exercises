from node import Node
from unorderedList import UnorderedList

def nodeTest():
	n1 = Node('A')
	print(n1.getData())
	n1.setData('B')
	print(n1.getData())

def unorderedListTest():
	ol = UnorderedList()
	ol.add('A')
	ol.add('B')
	print('a', ol.search('a'))
	print('B', ol.search('B'))

def unorderedListRemoveTest():
	print("remove")
	ol = UnorderedList()
	ol.add('A')
	ol.add('B')
	ol.add('C')
	ol.add('D')
	ol.add('E')
	ol.add('F')
	ol.add('G')
	ol.remove('A')
	ol.remove('B')
	printList(ol)


def unorderedListAppendTest():
	ol = UnorderedList()
	print("append")
	printList(ol)
	ol = UnorderedList()
	ol.append('B')
	ol.append('C')
	ol.append('B')
	printList(ol)

def unorderedListPopTest():
	print("pop")
	# ol = UnorderedList()
	# ol.append(1)
	# ol.append(2)
	# ol.add(-1)
	# while not ol.isEmpty():
	# 	print(ol.pop())
	# printList(ol)

	ol = UnorderedList()
	ol.append('A')
	ol.pop(0)
	printList(ol)

	# print(ol.pop(2))
	# print(ol.pop(0))

	# printList(ol)
	# print(ol.pop(0))
	# printList(ol)
	# print(ol.pop(0))
	# printList(ol)
	
def unorderedListInsertTest():
	ol = UnorderedList()
	ol.insert(0, 'G')
	printList(ol)
	ol.append('A')
	ol.append('B')
	ol.append('C')
	ol.append('E')
	ol.insert(3, 'D')
	ol.insert(0, 'F')
	printList(ol)

def unorderedListIndexTest():
	ol = UnorderedList()
	ol.insert(0, 'A')
	ol.append('B')
	ol.append('C')
	ol.append('D')
	ol.append('E')
	ol.append('F')
	ol.append('G')

	print(ol.index('G'))
	print(ol.index('A'))
	print(ol.index('I'))

def printList(ol):
	if not ol.head:
		print("list is empty")
	cur = ol.head
	while cur != None:
		print(cur.getData())
		cur = cur.next



def main():
	# nodeTest()
	# unorderedListTest()
	# unorderedListRemoveTest()
	# unorderedListAppendTest()
	unorderedListPopTest()
	# unorderedListInsertTest()()
	# unorderedListIndexTest()()



if __name__ == "__main__":
	main()
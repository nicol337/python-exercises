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
	ol = UnorderedList()
	ol.add('A')
	ol.add('B')
	ol.add('C')
	ol.add('D')
	ol.add('E')
	ol.add('F')
	ol.add('G')
	ol.remove('D')
	print(ol.items)


	

def main():
	nodeTest()
	unorderedListTest()
	unorderedListRemoveTest()


if __name__ == "__main__":
	main()
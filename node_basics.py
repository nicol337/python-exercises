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

	
def main():
	nodeTest()
	unorderedListTest()


if __name__ == "__main__":
	main()
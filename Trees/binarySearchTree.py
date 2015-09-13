class Node:
	def __init__(self,data):
		self.data = data
		self.leftChild = None
		self.rightChild = None


class BinarySearchTree: #assume no first empty search trees
	def __init__(self, node):
		self.root = node

	def addNode(self,node):
		currNode = self.root
		added = False
		while not added:
			if currNode.data == node.data:
				added = True
			elif currNode.data < node.data:
				if currNode.rightChild:
					currNode = currNode.rightChild
				else:
					currNode.rightChild = node
					added = True
			else:
				if currNode.leftChild:
					currNode = currNode.leftChild
				else:
					currNode.leftChild = node
					added = True

	def lookup(self,key):
		currNode = self.root
		parent = None
		while currNode:
			if currNode.data == key:
				return parent,currNode
			elif currNode.data < key:
				parent = currNode
				currNode = currNode.rightChild
			else:
				parent = currNode
				currNode = currNode.leftChild
		return None,None

	def delete(self,key):
		par, child = self.lookup(key)
		print(child.leftChild)
		if not (child.leftChild or child.rightChild):
			if par == None:	
				child.data = None
			elif par.leftChild == child:
				par.leftChild = None
			else:
				par.rightChild = None
		elif not child.leftChild:
			if None == par:
				self.root = child.rightChild
			elif par.leftChild == child:
				par.leftChild = child.rightChild
			else:
				par.rightChild = child.rightChild
		elif not child.rightChild:
			if None == par:
				self.root == child.leftChild
			elif par.leftChild == child:
				par.leftChild = child.leftChild
			else:
				par.rigthChild = child.leftChild
		else:
			currNode = child.rightChild
			while currNode.leftChild:
				currNode = currNode.leftChild
			newVal = currNode.data
			self.delete(currNode.data)
			child.data = newVal


	def DFS(self,node):
		print(node.data)
		if node.leftChild:
			self.DFS(node.leftChild)
		if node.rightChild:
			self.DFS(node.rightChild)

root = Node(10)
tree = BinarySearchTree(root)
for i in [5,8,7,3,2,9,12,11,24]:
	node = Node(i)
	tree.addNode(node)
if ((None,None) != tree.lookup(10)):
	print("Found!")
else:
	print("Not found!")
tree.DFS(tree.root)
print(tree.lookup((10)))
tree.delete(10)
tree.DFS(tree.root)













class BinaryTree:
	def __init__(self,obj):
		self.root = obj
		self.leftChild = None
		self.rightChild = None

	def insertLeftChild(self, obj):
		new_tree = BinaryTree(obj)
		if not self.leftChild:
			self.leftChild = new_tree
		else:
			new_tree.insertLeftChild(self.leftChild)
			self.leftChild = new_tree
	def insertRightChild(self, obj):
		new_tree = BinaryTree(obj)
		if not self.rightChild:
			self.rightChild = new_tree
		else:
			new_tree.insertRightChild(self.rightChild)
			self.rightChild = new_tree

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def setRootVal(self,obj):
		self.root = obj

	def getRootVal(self):
		return self.root






def printTree(btree):
	print(btree.getRootVal())
	if btree.leftChild:
		printTree(btree.getLeftChild())
	if btree.rightChild:
		printTree(btree.getRightChild())

def buildTree():
	mainTree = BinaryTree('a')
	mainTree.insertLeftChild('b')
	mainTree.insertRightChild('c')
	mainTree.getLeftChild().insertRightChild('d')
	mainTree.getRightChild().insertLeftChild('e')
	mainTree.getRightChild().insertRightChild('f')
	printTree(mainTree)


buildTree()


class Node:
	def __init__(self,data):
		self.data = data
		self.children = []

	def addChild(self,child):
		self.children.append(child)

	def __str__(self):
		return str(self.data)

class NaryTree:
	def __init__(self,root):
		self.root = root

	def preorderTraversal(self,node):
		print(node.data)
		for n in node.children:
			self.preorderTraversal(n)
	
	def postorderTraversal(self,node):
		for n in node.children:
			self.postorderTraversal(n)
		print(node.data)

	def BFS(self):
		""" Non recursive BFS """
		queue = [self.root]
		while queue:
			node = queue.pop(0)
			print(node)
			queue += [neighbor for neighbor in node.children]

	def DFS(self): 
		""" Non recursive DFS """
		queue = [self.root]
		while queue:
			node = queue.pop(0)
			print(node)
			queue = [neighbor for neighbor in node.children] + queue



root = Node("a")
tree = NaryTree(root)
for i,j in zip("bcd","efg"):
	n = Node(i)
	root.addChild(n)
	child = Node(j)
	n.addChild(child)

# tree.preorderTraversal(root)
# tree.postorderTraversal(root)
tree.BFS()
print("\n"*2)
tree.DFS()

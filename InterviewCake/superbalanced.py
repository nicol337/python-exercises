class Tree:
    def __init__(self, leftChild, rightChild):
        self.leftChild = leftChild
        self.rightChild = rightChild



leafDepth = -1

def findDepth(t, parentDepth):
    global leafDepth
    if t:
        tDepth = parentDepth + 1
        return findDepth(t.leftChild, tDepth) and findDepth(t.rightChild, tDepth)
    else:
        if leafDepth == -1:
            leafDepth = parentDepth
        return abs(parentDepth-leafDepth)<=1


# tree = Tree(None, None)
# tree2 = Tree(None, None)
# tree3 = Tree(None, None)
# tree4 = Tree(None,None)
# a = Tree(tree, tree2)
# b = Tree(tree3, tree4)
# c = Tree(a,b)

tree = Tree(None, None)
tree2 = Tree(None, None)
a = Tree(tree,tree2)
tree3 = Tree(None,None)
b = Tree(None, a)




print(findDepth(b, -1))
          
    
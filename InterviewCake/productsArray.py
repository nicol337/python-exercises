Interview Cake
Articles 
About
Upgrade
'sup Nicole.    Log out
Want help connecting with startups?
We work with companies in San Francisco, Silicon Valley and New York—big ones you know about, and small, upcoming ones. They're hiring both senior and junior candidates.

No guarantees, but let us know if you're interested and we'll see if we have something for you. Oh, and unfortunately we can't help with internships right now—only full-time.


Help me find a great startup!

× No thanks, not now
1
 2  3  4  5  6  7  8  
9
 10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  
26
 27  28  29  30  31  32  33  34  35  
36
 37  38  39  40  41  42  43
No more free questions left!

Upgrade Now 
Write a function to check that a binary tree ↴ is a valid binary search tree ↴ .
Gotchas
Consider this example:


Notice that when you check the blue node against its parent, it seems correct. However, it's greater than the root, so it should be in the root's right subtree. So we see that checking a node against its parent isn't sufficient to prove that it's in the correct spot.

We can do this in O(n)O(n) time and O(n)O(n) additional space, where nn is the number of nodes in our tree. Our additional space is O(\lg{n})O(lgn) if our tree is balanced.

Breakdown
One way to break the problem down is to come up with a way to confirm that a single node is in a valid place relative to its ancestors. Then if every node passes this test, our whole tree is a valid BST.

What makes a given node "correct" relative to its ancestors in a BST? Well, it must be greater than any node it is in the right subtree of, and less than any node it is in the left subtree of.

So we could do a walk through our binary tree, keeping track of the ancestors for each node and whether the node should be greater than or less than each of them. If each of these greater-than or less-than relationships holds true for each node, our BST is valid.

The simplest ways to traverse the tree are depth-first ↴ and breadth-first ↴ . They have the same time cost (they each visit each node once). Depth-first traversal of a tree uses memory proportional to the depth of the tree, while breadth-first traversal uses memory proportional to the breadth of the tree (how many nodes there are on the "level" that has the most nodes).

Because the tree's breadth can as much as double each time it gets one level deeper, depth-first traversal is likely to be more space-efficient than breadth-first traversal, though they are strictly both O(n)O(n) additional space in the worst case. The space savings are obvious if we know our binary tree is balanced—its depth will be O(\lg{n})O(lgn) and its breadth will be O(n)O(n).

But we're not just storing the nodes themselves in memory, we're also storing the value from each ancestor and whether it should be less than or greater than the given node. Each node has O(n)O(n) ancestors (O(\lg{n})O(lgn) for a balanced binary tree), so that gives us O(n^2)O(n
​2
​​ ) additional memory cost (O(n\lg{n})O(nlgn) for a balanced binary tree). We can do better.

Let's look at the inequalities we'd need to store for a given node:


Notice that we would end up testing that the blue node is <20, <30,and <50. Of course, <30 and <50 are implied by <20. So instead of storing each ancestor, we can just keep track of a lower_bound and upper_bound that our node's value must fit inside.

Solution
We do a depth-first walk through the tree, testing each node for validity as we go. A given node is valid if it's greater than all the ancestral nodes it's in the right sub-tree of and less than all the ancestral nodes it's in the left-subtree of. Instead of keeping track of each ancestor to check these inequalities, we just check the largest number it must be greater than (its lower_bound) and the smallest number it must be less than (its upper_bound).

  def bst_checker(root):
    # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    stack = Stack([(root, MIN_INT, MAX_INT)])

    # depth-first traversal
    while not stack.is_empty():
        node, lower_bound, upper_bound = stack.pop()

        # if this node is invalid, we return false right away
        if (node.value < lower_bound) or (node.value > upper_bound):
            return False

        if node.left:
            # this node must be less than the current node
            stack.push((node.left, lower_bound, node.value))
        if node.right:
            # this node must be greater than the current node
            stack.push((node.right, node.value, upper_bound))

    # if none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True
Instead of allocating a stack ourselves, we could write a recursive function that uses the call stack ↴ . This would work, but it would be vulnerable to stack overflow. However, the code does end up quite a bit cleaner:

  def bst_valid_recursive(root, lower_bound = MIN_INT, upper_bound = MAX_INT):
    if (not root):
      return True

    if (root.value > upper_bound or root.value < lower_bound):
      return False

    return bst_valid_recursive(root.left, lower_bound, root.value) \
      and bst_valid_recursive(root.right, root.value, upper_bound)
Complexity
O(n)O(n) time and O(n)O(n) additional space, where nn is the number of nodes in our tree. Our additional space is O(\lg{n})O(lgn) if our tree is balanced.

Did you get it right?

Yes, I'm expert on this Not quite, review later
Like this problem? Pass it on!
 Share  Tweet
 

Type code!
 
Copyright © 2015 Cake Labs, Inc. All rights reserved.
110 Capp St., Suite 200, San Francisco, CA US 94110 (804) 876-2253
Privacy | Terms
 

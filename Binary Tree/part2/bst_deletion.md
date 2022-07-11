# Binary Search Tree Node Deletion

---

## Theory

There are a few difference delete cases which we have to consider.

1. Delete node with no child:

In the case you have to delete a node with no children, i.e a node at the end of the tree for example, this is pretty straightforward. All you have to do is remove the node from the tree.

2. Delete node with one child:

In the case that you have to delete a node with only one child, all you have to do is delete that node, then move the child up into the place of the deleted node.

3. Delete node with two children:

In the case that you have to delete a node with a full sub-tree, one which has two child nodes, you have to make sure you re-balance the tree so that it still follows the rules of a binary search tree (smaller elements in the left sub-tree, larger elements in the right sub-tree).

### Methods for deleting node with two children:

Method 1:

The first method is to look at the right sub-tree relative to the deleted node, and then get the minimum value from the entire right branch. Then, you copy this branch into where the deleted node is. Finally, you remove the duplicate node with the same value, to follow the rules of binary search trees, which is that you can not have duplicate elements. Since the right sub-tree is always larger than the left one, and the minimum value of the right branch is smaller than all other ones in the branch, this means that when we move it to become the new parent node, it still has all smaller elements in its left sub-tree, and all larger elements in its right sub-tree.

Method 2:

The second method is the inverse of the first method, and involves looking at the left sub-tree relative to the deleted node, and then getting the maximum from the left branch. Then, you move that maximum into the location of the deleted node, and remove the duplicate node. Since the maximum value in the left sub-tree is larger than all other elements in the left sub-tree, and is stil smaller than all the elements in the right sub-tree, therefore, putting it as the new parent node still follows all of the rules of a binary search tree.

---

### Big O Complexity - time:

here

### Big O Complexity - space:

n/a

# Binary Tree

---

## What problem does it solve?

In most languages, there are data structures simillar to a set, which acts the same as an array/list, except, it can not have duplicate records; only unique instances of an element can occur in a set. Internally, one of the ways to implement a set, is a binary searech tree.

## What is it?

- A binary tree is nothing but a regular tree, with a constraint that it can have at most 2 child nodes, and generally will either have 0 or 2 children.

- A binary search tree is a special case of a binary tree, where the elements are ordered in a certain way where all elements to the left in a sub-tree are less than the root node, while all elements to the right in a sub-tree are greater than the root node.

### Levels

Like with a general tree, each sub-tree in a binary search tree is another level, starting from 0 to n. Therefore, the first root node is Level 0, then its sub-nodes are Level 1, then Level 2 etc.., until you reach the end of the tree.

---

## Common BST Operations

Some of the most common and important binary search tree operations include the following;

### Search Operation

In computer applications, search operations are very common, and a binary search tree offers an efficient and effective way to do this. Let's say your root node is 15, and you're looking for 11. You start by comparing 11 to 15, since its less, you go to the left sub-tree, then, compare that root node to 11, lets say 11 is greater, you go to the right sub-tree, then, keep doing this until you find 11 in the binary search tree.

### Insertion Operation

In the insertion operation with a binary search tree, you again, start at your root node, and we'll say that you're trying to insert 11 again. Starting at the root node of 15, since 11 is less, you move to the left side of the tree, then, you compare 11 to the new root node, if its less, you move to the left sub-tree, if greater, the right sub-tree. You keep doing this until there are no other sub-nodes, and you insert 11 either left or right to the current root node accordingly.

---

## Traversal Techniques (Breadth First Search vs Depth First Search)

Imagine a tree full of nodes. With depth first search, you pick a path, and traverse the whole path from top to the bottom most leaf, and then pick the next path and continue till all nodes have been visited. It is important to note that DFS is also _**recursive**_.

In the case of breadth first search, you start at top, and simply visit all the nodes at the same height, and then move on to the next lower level of nodes. Check out the wiki pages for both, they contain pretty good explanations and diagrams. It is important to note that BFS is also _**not recursive**_.

### Depth First Search

There are three ways to do depth first search, in-order traversal, pre-order traversal, and post-order traversal. All three of these traversals refer to the order of the root node in relation to the rest of the nodes in the tree. However, when visiting a sub-tree, the traversal is always left sub-tree, then right sub-tree.

- In-order traversal: visit your left sub-tree, then root node, then right sub-tree. **_ROOT NODE IN-BETWEEN LEFT AND RIGHT SUB-TREES_**
- Pre-order traversal: visit your root node, then right sub-tree, then left sub-tree. **_ROOT NODE BEFORE LEFT AND RIGHT SUB-TREES_**
- Post-order traversal: visit your left sub-tree, then right sub-tree then root node. **_ROOT NODE AFTER LEFT AND RIGHT SUB-TREES_**

---

### Big O complexity - time:

Search time complexity:

- Every iteration, we cut out either the larger half of the sub-tree, or smaller half of the sub-tree, therefore, each iteration, we reduce the search space by 1/2, so, our time complexity is O(log n).

Insertion time complexity:

- Insertion in a binary search tree is basically searching, and then inserting the element when and where there are no more elements remaining. Since with search, every iteration, we reduce the search space by 1/2, so, our time complexity for insertion is also O(log n).

### Big O complexity - space:

Space complexity for a binary search tree itself is proportional to the number of nodes in the tree. Hence, O(n)

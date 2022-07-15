# Heaps

---

## What are they?

A heap is essentially a specialized tree (binary search tree vs regular tree), which satisfies the heap property. A heap can come in two different versions, a min heap, or a max heap. A heap is a specialized tree-based data structure which is essentially an almost complete tree (A tree in which every level, except possibly the deepest, is entirely filled) that satisfies the heap property.

- In a max heap, for any given child node C, if P is its parent node, then the value of the parent node P, is greater than or equal to the value of the child node C. - In a min heap, the key of the parent node P, is less than or equal to the value of the child node C.

A heap can essentially be thought of as a tree, where in a min heap, we start with the smallest nodes in level 0, and then keep increasing in value towards level n; while a max heap starts with the largest node in level 0, and then keeps decreasing in value towards level n.

### Organization

A quick point to note is that although a heap is generally not as structured as other tree structures, if inserting two children, the smaller one gets inserted as the left sub-tree, while the larger one gets inserted as the right sub-tree.

## What are they used for?

Heaps are structures meant to allow quick access to the min or the max.

But why would you want that? You could just check every entry on add to see if it's the smallest or the biggest. This way you always have the smallest or the biggest in constant time O(1).

The answer is because heaps allow you to pull the smallest or the biggest and quickly know the NEXT smallest or biggest. That's why it's called a Priority Queue.

### Implemntation

A heap is a very intersting data structure as it is implemented using an array, with index 0 being the root (either the max or min), then index 1 being its smaller child, and index 2 being its larger child (or vice versa in a max heap). This keeps repeating, and a heap can be fully represented as such.

--> Given any index in a heap, you can access its parent, left child, and right child as such:

- Parent = (index-2) // 2
- Left Child = (index \* 2) + 1
- Right Child = (index \* 2) + 2

---

## Heap Operations

### Insertion

When inserting an element into a heap, you insert it into the first empty spot, first checking the left sub-tree, then the right sub-tree. Then, you bubble it up into whichever location insures that all elements below it are either smaller or larger than it depending on whether this is a min or max heap.

### Popping min or max

The most common opeartion on a heap is popping the top-most element (either the min or max depending on if min or max heap), from the heap. When we do this, we first take the value from the root node, then, we replace it with the value from the bottom most node in the heap. Now, we can quickly get the max using a simple array pop.

Now that we have popped from our array, we have to re-organize it again; so, we keep swapping the value downwards, until it is back in the correct location, and satisfies the heap property.

---

### Big O Complexity - time:

here

### Big O Complexity - space:

here

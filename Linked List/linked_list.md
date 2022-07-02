# Linked Lists

---

### Disadvantages of Arrays

The problem with arrays is that any proccess' done on the array are very slow, and require many computations. For example, if you want to insert an element at a specific index in an array, you have to swap each element one place after it. For deletion, its the same thing, you have to swap each item around it. In a linked list, you just insert it where it needs to be, without manipulating the entire array.

This is because in an array, when you reach the max of the initial memory allocation, you have to allocate double the memory capacity to that array, then copy all of the intial elements from the first memory location, to the new larger one. Then, let's say this was due to an insertion, you would have to then swap everything, to make space for this new element.

### Advantages of Linked Lists

Arrays store their data in one large data location, while a linked list just stores each piece of data randomly in data, wherever is free, and just has a refrence to the memory location of the next linked node. This means that any proccess' done on them are very fast, as you do not have to manipulate all of the data, all you do is modify the links. For example, if you wanted to insert a node, all you would have to do is change the link before it and after it, so that it is inserted where you want it to be in the list chain.

In summary, Linked Lists have two main benifits over arrays:

- You don't need to pre-allocate space, it is dynamically created as new nodes are added
- Insertion is easier, you don't have to swap elements around it, you just modify the links before and after where the node is inserted

## What are they?

In simple words, a linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list. Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a single large location; the elements are linked using pointers. They includes a series of connected nodes. Here, each node stores the data and the address of the next node.

---

### Doubly Linked List

A doubly linked list is simply a linked list which contains a pointer to both the next element, and the previous element. This allows for backwards traversal

---

### Big O Complexity - time:

Time complexities of some key linked list operations:

- Insertion / Deletion at beginning: O(1), just changing the head or tail note.
- Insertion / Deletion at end: O(n), you have to iterate through every single node to get to the end one.
- Insertion at middle: O(n): the more elements you have, the longer down the linked list you have to go to find the correct one.
- Traversal: O(n): the more elements you have, the longer it takes to traverse through them.
- Accessing element by value: O(n), since you have to search for the value through each element, the more elements you have, the longer the search proccess takes.

### Big O Complexity - space:

The space complexity of linked lists is O(n), as the more elements you have, the more space it takes up linearly.

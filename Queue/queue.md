# Queue

---

## What are they?

A queue is a collection of objects that supports fast first-in, first-out (FIFO) semantics for inserts and deletes. The insert and delete operations sometimes called enqueue and dequeue. Unlike lists or arrays, queues typically don't allow for random access to the objects they contain.

--> A queue can be thought of as a line-up, where the first person, or element in the line-up, is the first one served, or the first element that is retrieved from the queue.

--> You create an empty queue, then add the items all to it, then, when being retrieved, the first item that was inserted will be retrieved, then the second, etc.., till you reach the end of the queue.

### Producer / Consumer

The producer is the function, person, or object pushing data to the queue, while the consumer is the function, person, or object retrieving data from the queue.

---

### Implementations:

In python, there are three ways to implement a queue: list, collections.deque, and queue.LifoQueue.

- list: The problem with implementing a stack using a list is that internally, it is really just a dynamic array, meaning that it suffers from all the
  same downfalls as dynamic arrays. Namely, memory capacity is an issue, as it starts by allocating a capacity, then when an element
  surpasses this capacity, it doubles the capacity, then triples when that is surpassed, etc...
- collections.deque: The correct implemenation of a queue in python, internally, this is a doubly linked list, and as such, there is no issues with
  memory locations, nor is there any wasted memory unlike with using a list as an array.
- queue.FifoQueue: queue.FifoQueue is intended for allowing different threads to communicate using queued messages/data, and is not intended to be a data structure.

---

### Big O Complexity - time:

Some time complexities of queue operations:

- Insertion / Deletion: O(1), inserting or deleting something to or from an array is an O(1), or constant time operation, as it always takes the same time
  to retrieve or add something from or to the queue, no matter the data input size.
- Search by value: O(n), searching for an element by value in a queue is an O(n) operation, as you have to look through every single item to
  find the one with the desired value, and this scales lineary as more data is added.

### Big O Complexity - space:

The space complexity of queues is O(n), this is because as more data is inserted into the queue, the space that it takes up increases linearlly, and it requires more memory to hold all of the data.

---

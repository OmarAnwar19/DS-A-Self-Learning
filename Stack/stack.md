# Stack

---

## What are they?

A stack is a LIFO (last in, first out data structure), which allows you to store data in order of the last element inserted, to the first element inserted. A stack can be thought of as a shelf, where the items are placed from oldest at the back, to newest at the front, as items are pulled out from the front, the back items come to the front and replace them. When items are added to the shelf, or the stack, they are added to the very top of the stack.

--> In python, a stack can be implemented in 3 main ways: list, Collections.deque, queue.LifoQueue

### Operations

- Push: adds a new element to the top of the stack
- Pop: returns the last element added to the stack

### Use cases:

- Function calling in any programming language is managed using a stack, the first called function is at the bottom of the call stack, the last called function is at the top of the call stack.
- Undo functionality in a text editor uses stacks to track down the last edit
- The back button on a browser saves previous web pages in a stack, so they can be retrieved from most recently visited, to most distantly visited.

---

### Big O Complexity - time:

Some time complexities of stack operations:

- Push / Pop: O(1), pushing or popping something to or from an array is an O(1), or constant time operation, as it always takes the same time to retrieve or add something to the top of the stack, no matter the data input size.
- Search by value: O(n), searching for an element by value in a stack is an O(n) operation, as you have to look through every single item to find the one with the desired value, and this scales lineary as more data is added.

### Big O Complexity - space:

Stacks have an O(n) space complexity, as the memeory used increases linerally depending on the number of items in the stack.

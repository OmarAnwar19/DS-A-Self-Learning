# Arrays

## Info

Arrays are a way to store data, you store data in a group of data blocks, which can then be accessed using an index array[index_number].

- Each element in an array is stored within 4 bytes.
- Arrays can store any type of data, such as numbers, text, or even objects.
- Depending on the language, arrays can even hold mixed types (python can, java or c++ can't).
- Arrays can be multi-dimensional aswell (2d array = arr[][], 3d array = arr[][][])

### Static vs Dynamic Arrays

In languages such as Java and C++, there exists both static and dynamic arrays. You can either create an array with a set size (int[] arr = new int[5]), or an array with a dynamic size (ArrayList<Integer> arr = new ArrayList<Integer>()).

A _static_ array will only allocate the memory for that specific size, anything above that will not be inserted.

A _dynamic_ array will start by allocating a specific memory size, for example 10, it will keep inserting data into the array until the capacity of 10 is reached, then it will create a new static array in memory with double the capacity of the original array, and copy all of the elements to the new array (you do not see this in real time, this is just under the hood). Let's say you go past the new capacity of 20 elements, it will multiply the original capacity by 3 now, and repeat the process, etc.. to create enough space for the data you insert.
--> This proccess is known as **_Geometric Progression_**.

### Big O (time) complexity

An array has several different time complexities depending on the operation being preformed.

- Lookup by index (what is value for element at index 3 arr[3]): O(1), constant time --> as the size of the array increases, the time stays the same.
- Lookup by value (at what index is the value = 3?): O(n), linear time --> as the size of the array increases, the time increases proportionally (you have to look at every single item in the array to find the index with the value)
- Traversal (go through all the array, or print them all for example): O(n), linear time --> as the size of the array increases, the time increases proportionally (you have to access every single element)
- Insertion (you want to insert an element into the array at a specfic index arr.insert(index, value)): O(n), linear time --> as the size of the array increases, the time increases proportionally (when you insert a value, every other value has to be moved over, so n iterations)
- Deletion (you want to delete an element from the array at a specific index arr.remove(index)): O(n), linear time --> as the size of the array increases, the time increases proportionally (when you delete a value, every other value has to be moved over, so n iterations)

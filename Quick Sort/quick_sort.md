# Quick Sort

---

## How does it work?

We start by setting the first element as the pivot. Then, we move the pivot throughout the array, until we reach a point where every element on its left hand side is smaller than it, and every element on its right hand side is larger than it; now, the first part of the quick sort algorithim is done.
--> **_this proccess of putting pivots in the correct position is called partitioning_**

Now, we can think of the array as two parts, the smaller half to the left of the pivot, and the larger half to the right of the pivot. Then, we repeat the process from the first part using the left side; we get the first element, and move it to where every element to its left is smaller, and every element to its right is larger. We keep repeating this proccess with the left side, until it is fully sorted. If for example, the left half was still large, and was therefore cut into two, we would keep sorting the left most halfs, and then after doing those, we would do the right halfs of the left side. After the left side of the original pivot is sorted, we move onto the right side. We repeat the same proccess we did with the left side of the pivot on this side, moving the pivot to where everything on its left is smaller, and everything on its right is larger, and eventually, this will give us a fully sorted array.

**_NOTE:_** as is pretty obvious, quick sort is a recursive, divide and conquor sorting algorithim. We start with an array, and keep cutting it in half, recursively repeating the sorting proccess on each side, until the entire array is sorted.

---

## Partition Schemes

- Both of these schemes work to partition the array into a large and small half, but there are differences, aswell as pros and cons to each one.

### Hoare Partition

- In the Hoare partition scheme, the left most (first) element is the first pivot, and the second element is the start, while the last element is the end.

You start by setting the pivot, start, and end pointers, as noted above. Then, you begin the partitioning by moving the start pointer. It keeps moving untill it finds an element that is greater than the pivot value. The end pointer keeps moving until it finds an element that is less than the pivot value. Then, the two elements are swapped, and the pointers start moving again. The start pointer keeps moving again, until it finds an element greater than the pivot value, and the end pointer keeps moving until an element that is less than the pivot value is found, then they are swapped again. This proccess keeps going until the end pointer crosses the start pointer (no elements less than the pivot value on right, no elements greater than the pivot value on left), then it stops. When this occurs, you swap the pivot, and end pointer, and now the array is fully partitioned.

This proccess is then repeated for left side, right side, and for any time partitioning is required during the sort algorithim.

### Lomuto Partition

- In the Lomuto partition scheme, the right most (end) element is the first pivot, and the left most (first) element is the P(artition) Index.

You start by moving the P index until you find an element that is greater than the pivot value; at this point, a new counter is created at the next index after this one, called i. i keeps on moving until it finds an element that is less than the pivot. Then, you swap the current location of P index, and the current location of i. Then, at this point, you remove counter i, and start moving the P index again, until you find another element larget than the pivot, then, you create i again, and keep moving it until you find an element that is less than the pivot, and swap them. You repeat this procces until the pivot is the element which gets swapped, at this point, the entire array is partitioned.

**_NOTE:_** an easy way to describe this scheme, is that you keep moving the P index, and not worry about i, until you find an element greater than the pivot. Then, when this occurs, you create, and move the i, until you find an element less than the pivot. Then, you swap, and repeat (ignore i, move P index). You repeat this proccess until you get to, and swap the pivot, which then means that the array is fully partitioned.

---

### Big O Complexity: TIME

- The average time complexity of quick sort is O(n log n): this is because every time you partition the array, it gets split up n times, where n is depenedant on the length of the array.

- The worst time complexity of quick sort is O(n^2): this is beacuse if the array is already sorted, then it has to loop through every element twice, meaning n^2 time complexity.

### Big O Complexity: SPACE

- Since quicksort calls itself on the order of log(n) times (in the average case, worst case number of calls is O(n)), at each recursive call a new stack frame of constant size must be allocated. Hence the O(log(n)) space complexity.

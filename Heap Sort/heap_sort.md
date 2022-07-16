# Heap Sort

---

## What is heap sort?

In computer science, heapsort is a comparison-based sorting algorithm. Heapsort can be thought of as an improved selection sort: like selection sort, heapsort divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element from it and inserting it into the sorted region. Unlike selection sort, heapsort does not waste time with a linear-time scan of the unsorted region; rather, heap sort maintains the unsorted region in a heap data structure to more quickly find the largest element in each step.

## How does it work?

The steps are:

- Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O ( n ) {\displaystyle O(n)} O(n) operations.
- Swap the first element of the list with the final element. Decrease the considered range of the list by one.
- Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.
- Go to step (2) unless the considered range of the list is one element.

---

### Big O Complexity - time:

The heapify() method is called n-1 times. So the total complexity for repairing the heap is also O(n log n).

Both sub-algorithms, therefore, have the same time complexity. Hence:

The time complexity of Heapsort is:O(n log n)

### Big O Complexity - space:

Heapsort is an in-place sorting method, i.e., no additional memory space is required except for loop and auxiliary variables. The number of these variables is always the same, whether we sort ten elements or ten million. Therefore:

The space complexity of heapsort is: O(1)

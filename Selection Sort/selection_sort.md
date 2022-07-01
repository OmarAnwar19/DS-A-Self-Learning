# Selection Sort

---

## How does it work?

You start by finding the minimum value in the list, then, you swap that value, with whatever value is currently in the first index of the array, so that the smallest value in the array is now the first one. Then, you move along in your loop, and try to find the second smallest element other than the one we already sorted. Once found, you put that in the second index of the array. Then, you move on and find the third smallest element, and put it in the third index. You rpeat this proccess until you reach the end of the array, and it is now fully sorted.

---

### Big O Complexity - time:

The time complexity of selection sort is O(n^2), this is because we use two for loops in our program, and each time we get to a value, we have to do n^2 iterations.

### Big O Complexity - space:

The space complexity of selection sort is O(1), as you do not need to create any additional data structures to complete the sort algorithim.

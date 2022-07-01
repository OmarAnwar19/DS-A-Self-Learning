# Shell Sort

---

### What is it?

Shell sort is really just an optimized version of insertion sort. The problem with insertion sort is that it is extremly inefficient, as you have to keep comparing each element to the one before it, and when small elements are towards the end, it takes many comparisons and swaps to get the elements sorted in the correct positions.

### Insertion Sort Re-cap

Recall that in regular insertion sort, you start with the second element, then compare it to the first one, if smaller, you insert it behind it. Then, you go to the third element, and compare it to the second and first, and insert it where all the elements to its left are smaller, and the elements to its right are larger. You keep repeating this proccess until the entire array is sorted.

## How does it work?

In shell sort, you start by trying to move all of the larger elements to the right side of the array, so that there are less comparisons required to sort the array when it gets to the smaller elements.

So, you start with your first number, and the element at a fixed gap - your anchor. That is your first pair. Next, you get the element after your first number, and the element after your anchor, that is your second pair. Then, you get the element after those two, and that is your third pair. You keep pairing these elements until you reach the end of the array. Then, you swap the pairs so that the smaller one is on the left, and the larger one is on the right. Then, you reduce the gap by n // 2, and repeat the proccess. You keep repeating until your gap is 1, where you just do regular insertion sort. At this point, your entire array is sorted.

### What's the point?

After doing the shell sort proccess up until gap size 1, you are moving all of the smaller elements to the left side, and all of the larger elements to the right side. By doing this, one you reach gap size 1, and do regular insertion sort, there are much less comparisons and swaps which need to be preformed to sort the array when compared to regular insertion sort.

---

### Big O Complexity - time:

The worst time complexity of shell sort is O(n^2), this is because we have to use two loops for each element, to create the gaps, then sort the array. The average time complexity of shell sort is

### Big O Complexity - space:

The space complexity of shell sort is O(1), this is because you do not need to create any new structures as the size of the array increases, only the original array itself.

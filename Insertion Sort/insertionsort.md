# Insertion Sort

## How does it work?

We start from the second element of the array, as the first one is automatically sorted. Then, we compare the second one to the first one, if its less, then we insert it in the first slot. Then, we check the third element, if its less than the second element, we check the first element, and if its less, we insert it in the first spot, if not, that means we insert it in the second slot. Then, we go to the fourth element and compare it to the third slot, if smaller, we compare it to the second, etc.. until the element to its left is not smaller, and we then insert it at that spot. We then repeat the process for the fifth element, then sixth, etc.., until the entire array is sorted.

## Big O (time) complexity

Since we have to use two loops (1 for loop and 1 while loop), the time complexity of insertion sort is: O(n^2).

## Space complexity

Insertion sort only requires us to create one variable for the pointer elment, so space complexity is O(1).

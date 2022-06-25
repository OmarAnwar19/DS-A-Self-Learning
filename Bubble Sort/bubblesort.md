# Bubble Sort

## How does it work?

We start by comparing the first two elements in an array,
the larger of the two elements gets swapped into the second position.
Then, we compare elemnt two and three, and the larger one gets swapped
to the third position. Then we compare elements three and four, then four
and five, etc.. until we reach the end of the array.

As soon as we can no longer swap two elements, that means the larger element
of the first two, is in the correct positoin.

Now, we repeat the proccess with the first two elements again (they are now different).
And we keep repeating this process, with each element, untill they are all sorted
in the correct order.


## Big O (time) complexity

Since we have 2 for loops running at the same time, Big O complexity is:
O(n^2)

## Space complexity

Since we are not using any additional space other than our original array,
space complexity is: O(1)

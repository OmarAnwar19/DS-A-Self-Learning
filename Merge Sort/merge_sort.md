# Merge Sort

### pre-info: what if we have two sorted arrays, and we want to merge them into one sorted array?

Let's say you have two sorted arrays, and you want to combine them into one sorted array, what do you do? You create a new array, and start with two pointers at the first element of both arrays, then, you compare the first element of each array to eachother, the smaller element gets put into the new array. After doing this, you move the pointer of the array where the smaller element was, right by one. Then, you compare the elements at the pointer again, the smaller one gets inserted, and the pointer of the array where the smaller one was, gets moved over right by one. You do this until the pointer can no longer move over to the right, which means the array is merged and sorted.

## How do we use this to sort an un-sorted array?

First, we have to realize that with an unsorted array, the merge from pre-info would not work, as our comparison would not sort them. So, we first have to make it so we can compare elements to get the smaller one. We start by recursivley breaking up the array into half, and then our half into quarters, and then those into eights, etc.. until the entire array is broken down into arrays of one element each. Then, we can start the merge sort proccess. Let's say we now have 8 individual arrays, we start by comparing the first two arrays, and then merging them together in order. Then, we move to arrays 2 and 3, and compare which is bigger, and merge sort them together. We do this until all the arrays are merged into sorted groups of two arrays (4 arrays of 2 elements each). Next, we do the same thing with the arrays of two, this time how we did it in pre-info. We compare the first element of arrays 1 and 2, and place the smaller one at the beginning, then move the pointer in its array. Then, we compare the next two elements and repeat this process, until these two arrays are sorted. We then repeat the proccess with arrays 3 and 4, until they are also merged and sorted. We now have 2 sorted arrays left. Now, for the final step, we repeat the merge sorting process with pointers and comparison, to combine these final 2 arrays, and this will give us one final sorted array.

### Big O (time) complexity

The time complexity of merge sort is O(n log n), as the time it takes to preform merge sort increases exponentially by a constant of 2, as you have to break down the array into half partitions each time, which increases exponentially as you add more items to the dataset.

### Space complexity

The space complexity of merge sort is O(n), where n is the number of elements in the array. This is beacuse each element has to be copied into its own array during the divide proccess, so we need n amount of arrays, or n space.

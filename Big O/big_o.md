# Big O Notation (time/space complexity)

## What is Big O notation

## Big O for time complexity

**_definition:_** Big O notation is used to measure how running time or space requirements for your program grow as input size grows.

As the input size of a function grows, generally, so does its run time or space requirements. A linear function runs in a\*n + b time, where a is the constant number of arrays, n is the number of elements in the array, and b is the starting run time or space of the algorithim. For Big O notation, we drop constants, so we get rid of a and b, and then add an O around our remaining term. So, our run speed or space required for the algorithim is now O(n); pronounced as Order of (n).

**_NOTE:_** an important rule to note is that with Big O notation, you always keep the biggest run time or space. So, for example, if we have a function with two logic blocks, one which runs at n^2 iterations, and one which runs at n iterations, the run time of the entire function is the larger value, so O(n^2). This is beacuse Big O calculates an arbitrarily large number of iterations, so, in the largest time scenario, the smaller run time is irrelevant, so it is discounted.

### Some common complexities:

_Each such notation defines the SHAPE of a curve. The curve shape indicates the relationship between the SIZE of a dataset (amount of data) and the TIME it takes to process that data. (Or the amount of memory when concerned about space optimization.) In other words, these show how performance degrades as the dataset gets bigger._

O(n): linear run time / space complexity, as the number of inputs increases, the time or space increases linearly (500 items = 500 computations)

O(1): constant run time / space complexity, as the number of inputs increases, the time or space stays (pretty much) the same

O(n^2): quadratic run time / space complexity, as the number of inputs increases, the time or space stays the same; this example is n^2 due to the fact that it has a nested loop. Each time another loop is nested, the n^2 increases. So, three loops would be O(n^3), four would be O(n^4), etc...

O(log n): logarithmic run time / space complexity, as the number of inputs increases, the time or space goes up exponentially. So for example, plugging in log 10 on a calculator gives 1, log 100 gives 10, and log 1000 gives 3. Simillarly, O(log n) run time means that run time increases exponentially to the number of elements inputted; 10 inputs would take 1ms, 100 would take 2ms, etc... This run time usually occurs in divide and conquor algorithims; each level contains double the inputs as the previous.

O(n log n): multiple logarithimic run time / space complexity: as the number of inputs increases, the time or space goes up exponentially by a constant. It just means that an algorithim increases exponentially by the number of elements created by said algorithim. For example, merge sort is O(n log n) run time, because it increases exponentially by a constant, as you have to split the array in half over and over, so n \* logn.

# Binary Search

---

### Overview of Linear Search

In a normal colleciton of data, if we want to find a specific item, we can use linear search to iterate over every item in the collection, and return the index of the search item if its value is equal to the value of the current item in iteration.

However, this is not very efficient, as its time complexity is O(n), meaning that we have to check every single element in order to find a search element.

---

## Overview of Binary Search

**Binary search allows you to find an element in a **_sorted_** array.**

When compared to linear search, instead of iterating through every single element looking for a value, instead, what we can do is preform a technique simillar to merge sort.

We check the middle element of the array, and then if the serach element is greater than it, we look at the right side of the array. If it is smaller, we look at the left side of the array. Then, we look at the middle of that half of the array, and repeat the proccess of checking if the search value is smaller or larger. We keep doing this process, of cutting the array in half, until we eventually find the actual element which we are looking for.

---

## Implementations

There are two distinct implementations of binary serach, iterative, and recursive.

Both will have the same time complexity O(log(n)), but they will different in term of space usage. Recursive may be "log(n)" space (because of the stack), in iterative BS it should be "O(1)" space complexity.

At the point of choice of recursive vs. iterative formulation is pretty much a matter of personal and local preference. Some people find recursive code easier to understand. Some people are scared to death of recursion, or don't understand it, or have no clue about tail recursion optimization, and want explicitly iterative code everywhere.

### Iterative Implementation

The steps of iterative binary search are as follows: - The main() method of IterativeBinarySearch class starts off with defining a Array, named A. - Key is the number to be searched in the list of elements. - Inside the while loop, "mid" is obtained by calculating (low+high)/2. - If number at position mid equal to key or target element then the control returns index of mid element by printing that the number has been found along with the index at which it was found.

    -  *Else, if key or target is less than number at position mid then the portion of the Array from the mid upwards is removed from contention by making "high" equal to mid-1.
    - Else, it implies that key element is greater than number at position mid(as it is not less than and also not equal, hence, it has to be greater). Hence, the portion of the list from mid and downwards is removed from contention by making "low" equal to mid+1.

    - The while loop continues to iterate in this way till either the element is returned (indicating key has been found in the Array) or low becomes greater than high, in which case -1 is returned indicating that key could not be found and the same is printed as output.

### Recursive Implementation

Recursive implementation of binary search algorithm, in the method binarySearch(), follows almost the same logic as iterative version, except for a couple of differences.

The steps of recursive binary search are as follows: - The first difference is that the while loop is replaced by a recursive call back to the same method with the new values of low and high passed to the next recursive invocation along with "Array" and "key" or target element. - The second difference is that instead of returning false when the while loop exits in the iterative version, in case of the recursive version, the condition of low > high is checked at the beginning of the next level of recursion and acts as the boundary condition for stopping further recursive calls by returning false. - Also, note that the recursive invocations of binarySearch() return back the search result up the recursive call stack so that true or false return value is passed back up the call stack without any further processing.

---

### Big O Complexity - time:

Every iteration of binary search, we divide the search area by half, meaning that it takes iteartion k = n/2^k. Therefore, the time complexity of binary search is O(log n), since the time complexity increases logorithmically as more elements are added.

### Big O Complexity - space:

In an iterative implementation of Binary Search, the space complexity will be O(1).
--> This is because we need two variable to keep track of the range of elements that are to be checked. No other data is needed.

In a recursive implementation of Binary Search, the space complexity will be O(logN).
--> This is because in the worst case, there will be logN recursive calls and all these recursive calls will be stacked in memory. In fact, if I comparisons are needed, then I recursive calls will be stacked in memory and from our analysis of average case time complexity, we know that the average memory will be O(logN) as well.

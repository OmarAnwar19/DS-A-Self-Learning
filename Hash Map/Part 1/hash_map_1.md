# Hash Map/Table PART 1 (basics)

---

## What are they?

Basically, a HashMap allows you to store items with identifiers. They are stored in a table format with the identifier being hashed using a hashing algorithm. In python, a dictionary is just an implementation of a HashMap.

### Array vs Hashmap

Let's say we wanted to find a price on a specific date, if we were to do that with an array, the search proccess would be O(n), since we have to through each element until we reach the specific date. On the other hand, in a hash map, the look up would only be O(1), since we access the specifc date (prices[date] = price we are looking for)

This is beacause in memory, an array of arrays stores each key and value in individual memory indexes, while a dictionary will store the pair in random, non contiguous data locations, so we can just refrence the key and value pairs whenever we need them.

### Hash Functions

To get the values of each key in a dictionary or hash map, we have to use one of many hash functions. One such example is ascii storage, where each letter in the key name is refrenced with its ascii value, and then all of the values of the key are added up. Then, on retrieval, it unwinds this, to get the key value pair.

_**a hashmap really just takes a key, hashes it, then puts it into an array with a value corresponding to that hashed key; this hashing proccess is what makes it so fast and efficient when compared to an array.**_

---

### Big O Complexity - time:

Some of the big o complexites of HashMap functions:

- Lookup by key: O(1), you just get the value at the key linearly hashmap[key]
- Insertion / Deleting: O(1), you just get the value at the key linearly hashmap[key] and delete or insert at it

### Big O Complexity - space:

Hashmaps generally have a Big O Space complexity of O(n), because as you increase the number of keys, and values, you have to linearly add space in memory.

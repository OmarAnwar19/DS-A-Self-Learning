# Hash Map/Table PART 2 (collisions)

---

## Seperate Chaining

At times, when storing hashed values, we might get an identical hash value, meaing that they will be stored in data at the same location. This can cause an error if not handled.

One way to handle this is with seperate chaining. This is when instead of direcly storing the value in memory, we store a list of a key value pair. Therefore, each time a collision occurs, all we have to do is append the key value pair to this list, and there will no longer be a problem.

### Big O Complexity - time:

Unlike a normal hash map, where we just get the value directly in O(1) time, seperate chaining can up the time complexity to O(n). This is because in certain scenarios, lets say every single value had an identical value, we might have to check every value in the list at a location until we find the correct one.

---

## Linear Probing

The second approach to handle collisions is when we get a hashed value, which when cross refrenced with memory we find out allready has another key in that location, what we do is we go to the next available memory location, and we keep doing this until we find the nearest empty memory location, where we store the key value pair.

### Big O Complexity - time:

Like seperate chaining, in the worst possible scenario where each memory location near by already has data in it, we might have to iterate over every single key value pair in memory until we reach the end, which would bring us to O(n) time complexity.

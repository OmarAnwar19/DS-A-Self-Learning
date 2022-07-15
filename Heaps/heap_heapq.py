# in python, the easiest way to use a heap, is to use heapq (rather than implement it)
#!! NOTE: heapq only implements a min heap !!!
import heapq


# * although you can use heapq on its own, a more practical way would be to create a MinHeap class
class MinHeap:
    def __init__(self) -> None:
        self.data = []

    def peek(self):
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)

    def get(self):
        return self.data


# * although it does not inherently support it, a maxheap can be created as such
class MaxHeap:
    def __init__(self):
        self.data = []

    def peek(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)

    def get(self):
        return self.data


# using heapq on its own (without classes)
def heapq_functions():
    # to create a new heap, simply create an empty array
    heap = []

    # then, to add an item to the heap, use heapq.heappush(heap, item)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 18)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 6)
    heapq.heappush(heap, 15)

    # we can then display the heap by simply printing the list
    print(f"heap: {heap}")

    # we can pop an element from the heap using heapq.heappop
    min_pop = heapq.heappop(heap)
    print(f"min: {min_pop}")

    # a simillar method is heapq.heappushpop, to pop the element from the top of the list, and also push another element to it
    min_pushpop = heapq.heappushpop(heap, 8)
    print(f"popped: {min_pushpop}, new heap: {heap}")

    # we can also get the n largest or n smallest items from a heap using heapq.nlargest / nsmallest
    three_largest = heapq.nlargest(3, heap)
    three_smallest = heapq.nsmallest(3, heap)

    print(f"three_largest: {three_largest}")
    print(f"three_smallest: {three_smallest}")

    # we can also take a normal list, and heapify it
    arr = [9, 12, 2, 45, 6, 3, 8, 22]
    # all we do is heapq.heapify(arr)
    heapq.heapify(arr)

    print(f"arr heapified: {arr}")


# using heapq with classes (MIN HEAP IMPLEMENTATION)
def heapq_min_class():
    # --- MINHEAP ---

    # create a min heap using min heap class
    min_heap = MinHeap()

    # add items to the heap using .push
    min_heap.push(5)
    min_heap.push(12)
    min_heap.push(7)
    min_heap.push(23)
    min_heap.push(22)

    # we can use .peek to check the top value
    print(f"peek: {min_heap.peek()}")

    # we can use .pop to get the top value
    top = min_heap.pop()
    print(f"top: {top}")

    # then, we can print the heap by simply printing the min_heap.get()
    print(min_heap.get())


# using heapq with classes (MAX HEAP IMPLEMENTATION)
def heapq_max_class():
    # --- MAXHEAP ---

    # create a max heap using max heap class
    max_heap = MaxHeap()

    # add items to the heap using .push
    max_heap.push(5)
    max_heap.push(12)
    max_heap.push(7)
    max_heap.push(23)
    max_heap.push(22)

    # we can use .peek to check the top value
    print(f"peek: {max_heap.peek()}")

    # we can use .pop to get the top value
    top = max_heap.pop()
    print(f"top: {top}")

    # then, we can print the heap by simply printing the max_heap.get()
    print(max_heap.get())


if __name__ == "__main__":
    print("\n--- HEAPQ FUNCTIONS ---\n")
    heapq_functions()

    print("\n--- MIN HEAP CLASS ---\n")
    heapq_min_class()

    print("\n--- MAX HEAP CLASS ---\n")
    heapq_max_class()

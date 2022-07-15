# class for an implementation of a minHeap
class minHeap:
    # init the heap
    def __init__(self) -> None:
        # all we do is create an internal array, which will hold all of the heap values
        self.heap = []

    # internal helper functions (only meant to be used by class itself)

    # helper function to swap the values at two indexes
    def __swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    # helper function to float elements up the heap
    def __float(self, i):
        # first, get the index of the parent index of the current i
        P_i = self.parent_i(i)

        # if the i we passed in is <= 1 (we are at beginning of heap)
        if i == 0:
            # return from the function, no need to swap anymore
            return
        # otherwise, if the value in the heap at the index of i is greater thatn value in heap at index of parent
        # --> this means we have to swap the two indexes, then float the parent up
        elif self.heap[i] < self.heap[P_i]:
            # swap the values at index i, and parent index
            self.__swap(i, P_i)
            # then, call float again on parent index, to check if its less or greater than its parent
            self.__float(P_i)

    # helper function to min_heapify a value(insert it in the correct location in the heap)
    def __min_heapify(self, i):
        # when min heapifying, you have to get the min value between parent and children, then insert it highest up

        # so, first get the indexes of the left and right children of index i
        L_i = self.child_left_i(i)
        R_i = self.child_right_i(i)

        # then, we can start the min index as the index that we passed in
        min_i = i

        # first we check if the heap is not at the end,
        # then, we check if the value at the current min_i is less than the value at its left child
        # if it is, that means we have to set its left child as the new min index
        if len(self.heap) > L_i and self.heap[min_i] > self.heap[L_i]:
            min_i = L_i

        # same as above, but checking right child
        if len(self.heap) > R_i and self.heap[min_i] > self.heap[R_i]:
            min_i = R_i

        # after we get the min index, we have to make sure its not still i, because swapping would be redundant if so
        if min_i != i:
            # so, swap the values at i and min_i
            self.__swap(i, min_i)
            # then, call min_heapify on min_i, which will keep checking if anything is larger than it, until we reach top of heap
            self.__min_heapify(min_i)

    # helper functions for getting indexes of parent and child nodes

    # get the parent index based on an inputted index
    def parent_i(self, i):
        # return (i-1) / 2, which gives you the index of the parent
        return (i-1) // 2

    # get the left child index based on an inputted index
    def child_left_i(self, i):
        # return 2*i + 1, which gives you the index of the left child
        return 2*i+1

    # get the right child index based on an inputted index
    def child_right_i(self, i):
        # return 2*i + 2, which gives you the index of the right child
        return 2*i+2

    # peek function (look at top of heap)
    def peek(self):
        # if a value exists at index 0 of the heap,
        if self.heap[0]:
            # return that value
            return self.heap[0]
        # otherwise, return False
        else:
            return False

    # function to add a node to the heap
    def push(self, data):
        # add the data to the internal heap array
        self.heap.append(data)
        # call the function to float the value at the last index to its correct location
        # (since we appended data to array, its the data we just put)
        self.__float(len(self.heap) - 1)

    # function to add a list of nodes to the heap
    def push_items(self, arr):
        # loop over each item in the inputted array
        for item in arr:
            # call the push function on each item to add it to the internal array
            self.push(item)

    #function to pop the min value from the heap
    def pop(self):
        #first, we have to check if the heap is empty, 
        if len(self.heap) == 0:
            #if it is, return False, as there is nothing to return
            return False        
        #then, we check if the heap has exactly one element in it,
        elif len(self.heap) == 1:
            #if so, then just return the top element of the heap
            return self.heap.pop()
        #if neither of these conditions are true, that means the heap has multiple elements, 
        #--> so, we have to do the whole proccess for popping
        else:
            #as we remember, when we pop an element from a heap, we first swap the top and bottom elements in the heap
            #--> so, call the swap function on the value at index 0, and value at last index in heap
            self.__swap(0, len(self.heap) - 1)
            #then, since we just swapped the min value to the top of the heap, we can return the min by simply popping it from the heap
            min = self.heap.pop()
            #then, we have to min_heapify the rest of the heap, so that it is sorted again
            #--> so, we call min_heapify on index 0, so that the entire heap is re-organized
            self.__min_heapify(0)
            
        #return the min value
        return min
    
    #function to delete an element from a heap by index
    def remove(self, i):
        #delete the value from the index in the internal heap
        del self.heap[i]
        #then, min_heapify at index 0, so that everything is sorted again
        self.__min_heapify(0)
        
    #funtion to return the actual heap
    def get_heap(self):
        #all we do is return the internal heap container
        return self.heap


if __name__ == "__main__":
    #create a new min_heap by calling the minHeap class
    min_heap = minHeap()
    
    #then, we can add some values to the heap
    min_heap.push(10)
    min_heap.push(15)
    min_heap.push(20)
    
    min_heap.push_items([1,2,3,4,5])
    
    #then, we can print the heap
    print (min_heap.get_heap())
    
    #we can also peek at the heap
    min_peek = min_heap.peek()
    print (min_peek)
    
    #we can also remove an element in the heap
    print (f"before delete: {min_heap.get_heap()}")
    min_heap.remove(3)
    print (f"after delete: {min_heap.get_heap()}")
    
    #or, we can pop the top element from the heap
    min_pop = min_heap.pop()
    print (f"top pop: {min_pop}")
    

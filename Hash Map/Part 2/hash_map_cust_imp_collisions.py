# NOTE: THIS IS JUST THE IMPLEMENTATION OF THE INNER WORKINGS OF A HASH TABLE
#       IN PRACTICE, YOU WOULD JUST USE THE DICTIONARY IN PYTHON
# !! THIS FILE INCLUDES COLLISION HANDLING !!


class HashTable:
    def __init__(self, MAX) -> None:
        self.MAX = MAX
        # the first difference is that we initialize an empty array for each element, instead of None
        self.arr = [[] for i in range(self.MAX)]

    # function to hash the key
    def get_hash(self, key):
        hash = 0

        for char in key:
            hash += ord(char)

        return hash % 100

    # functin to add a value to the hash map at a key value pair
    def __setitem__(self, key, val):
        # get the hashed key
        hash = self.get_hash(key)

        # create a found variable to check if we key value pair already exists in table
        found = False

        # there are a few different set item conditions we can do with the new implementation
        # first, lets say there are multiple items, and the first one needs to be updated
        for index, el_list in enumerate(self.arr):
            # so, if the length of the element list is 2, the item at the first index in the list is the value to update
            if len(el_list) == 2 and el_list[0] == key:
                # we update the element list at the correct location at the current hash index with the key value pair
                self.arr[hash][index] = (key, val)
                # then, we set the found variable to true
                found = True
                # and break the loop, we already did what we wanted
                break

        # if found is still false, that means value does not already exist, so,
        if not found:
            # append the key value pair to the hash
            self.arr[hash].append((key, val))

    # function to get a value from hashmap using a key
    def __getitem__(self, key):
        # get the hashed key
        hash = self.get_hash(key)

        for el in self.arr[hash]:
            if el[0] == key:
                return el[1]

    # function to delete an item by key
    def __delitem__(self, key):
        hash = self.get_hash(key)

        for index, value in enumerate(self.arr[hash]):
            if value[0] == key:
                del self.arr[hash][index]


if __name__ == "__main__":
    # create a new hash table object
    hash_map = HashTable(100)

    # set some values in the hashmap
    hash_map["my first key"] = 100
    hash_map["my second key"] = 500
    hash_map["my third key"] = 1500

    # retrieve some values from the hashmap
    print(hash_map["my first key"])
    print(hash_map["my second key"])
    print(hash_map["my third key"])

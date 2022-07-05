# NOTE: THIS IS JUST THE IMPLEMENTATION OF THE INNER WORKINGS OF A HASH TABLE
#       IN PRACTICE, YOU WOULD JUST USE THE DICTIONARY IN PYTHON


# the class for our custom hashmap
class HashTable:
    # our init function, takes in a max length var
    def __init__(self, MAX) -> None:
        # set the max as the one we took in
        self.MAX = MAX
        # create an empty array by looping to self.MAX, and adding None at each index
        self.arr = [None for i in range(self.MAX)]

    # function to hash the key
    def get_hash(self, key):
        # variable for the hash value of the key
        hash = 0

        # loop over each character in key
        for char in key:
            # add the ascii code corresponding to the character to hash
            hash += ord(char)

        # finally, return the hash divided by 100 (so its easy to parse)
        return hash % 100

    # these right here are proper functions, however they require use of map.add and map.get()
    # more convenient if we could just do map[key] or map[val]
    # # function to add a key value pair to hashmap
    # def add(self, key, val):
    #     # hashes the key
    #     hash = self.get_hash(key)
    #     # adds the value to the array at the key of hash
    #     self.arr[hash] = val

    # # function to get a value from hashmap using a key
    # def get(self, key):
    #     # get the hashed key
    #     hash = self.get_hash(key)
    #     # return the value at the hashed key from the array
    #     return self.arr[hash]

    # the only difference is we change add to __getitem__ and get to __getitem__
    # function to add a key value pair to hashmap
    def __setitem__(self, key, val):
        # hashes the key
        hash = self.get_hash(key)
        # adds the value to the array at the key of hash
        self.arr[hash] = val

    # function to get a value from hashmap using a key
    def __getitem__(self, key):
        # get the hashed key
        hash = self.get_hash(key)
        # return the value at the hashed key from the array
        return self.arr[hash]

    # function to delete an item by key
    def __delitem__(self, key):
        # get the hashed key
        hash = self.get_hash(key)
        # set the value of the hashed key in the array = None,
        # this is equivelant to clearing it from memory, effecively deleting it
        self.arr[hash] = None


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

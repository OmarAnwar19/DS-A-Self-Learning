class Node:
    # each node in a linked list has a piece of data, and a pointer for the next node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# a linked list is made up of a list of nodes
class LinkedList:
    # each linked list has a head node, which is the first node in the list
    def __init__(self):
        self.head = None
        self.tail = None

    # first method is to insert the head
    def insert_head(self, data):
        # we create a new node, passing in data=data, and the current head as the net node
        # --> this is because if we insert a new head, that means the old head is pushed over one
        node = Node(data, self.head)
        # then, we set the new head as the one we just created
        self.head = node

    # method to insert data at end of linked list
    def insert(self, data):
        # the first thing you do is create a new node object using data taken in
        new_node = Node(data)

        # then, we have to check if a list head already exists, if not, set the new node as the head
        if self.head is None:
            self.head = new_node
            # then, break the loop
            return

        # otherwise, if head already exists, we have to iterate to end of list, and add new node there

        # the first thing we do, is set the current node as the head
        curr_node = self.head

        # then, we have to iterate to the end of the list
        # so, while the current node has a next value (while list is not at end)
        while curr_node.next:
            # set the current node as the relative next one
            curr_node = curr_node.next

        # once we have gotten to the final node in the list, add the new node as its next value
        curr_node.next = new_node
        # then, add the new node as the tail
        self.tail = new_node

    # method to insert multiple values to the list
    def insert_values(self, data_list):
        # loop over each data item in the data_list
        for data in data_list:
            self.insert(data)

    # method to insert data at a specific index
    def insert_index(self, insert_index, data):
        # the first thing we have to do is check that the index is valid
        # --> have to make sure that index is not less than 0, and not greater than the length of the list
        if insert_index < 0 or insert_index >= self.get_len():
            # if the index is invalid, return an error, "Invalid Index"
            raise Exception("Invalid Index")

        # if the user is trying to add the head
        if insert_index == 0:
            # all we have to do is call the insert_head function, passing in the data
            self.insert_head(data)
            # then, return from the loop
            return

        # after we have checked the previous things, we can do a normal insert at index

        # the first thing we do is create a variable for the index of the current node loop
        i = 0
        # we start by setting the current node as the head
        curr_node = self.head

        # then, we loop as long as the current node has a next value (we have not reached end of list)
        while curr_node:
            # if the next index is the one to be removed
            if i+1 == insert_index:
                # first, get the next node
                next_node = curr_node.next

                # then, create a new node, with data, and the next node relative to the current one as its next pointer
                new_node = Node(data, next_node)

                # then, set the next pointer of the current node, as the new one we just created
                curr_node.next = new_node

                # finally, break out of the loop
                break

            # if the current node is not the one we want to insert after, set the new current node as the next one
            curr_node = curr_node.next
            # then, increment the value of the i counter by 1
            i += 1

    def get_len(self):
        # first, we create a variable for the node count
        count = 0

        # then, we set the starting node as the head node
        node = self.head

        # then, we loop as long as node.next exists (loop until end of linked list)
        while node:
            # while this is true:
            # first, add 1 to the count variable
            count += 1
            # then, go to the next node using curr_node.next
            node = node.next

        # finally, after we have counted all of the nodes, return the count variable
        return count

    # method to remove data at a specfic index in the list
    def delete_index(self, remove_index):
        # the first thing we have to do is check that the index is valid
        # --> have to make sure that index is not less than 0, and not greater than the length of the list
        if remove_index < 0 or remove_index >= self.get_len():
            # if the index is invalid, return an error, "Invalid Index"
            raise Exception("Invalid Index")

        # if the user is trying to remove the head
        if remove_index == 0:
            # all we have to do is change the head to the second element in the list
            # this will severe the refrence to the original head, and set the new one as the second element
            self.head = self.head.next
            # then, return from the loop
            return

        # after we have checked the previous things, we can do a normal delete at index

        # the first thing we do is create a variable for the index of the current node loop
        i = 0
        # we start by setting the current node as the head
        curr_node = self.head

        # then, we loop as long as the current node has a next value (we have not reached end of list)
        while curr_node:
            # if the next index is the one to be removed
            if i+1 == remove_index:
                # first, get the next node
                next_node = curr_node.next

                # then, set the next node of the current node as the next node of the next node
                # basically, you remove the actual next node by linking the current one, and the node 2 ahead
                curr_node.next = next_node.next

                # finally, break out of the loop
                break

            # if the current node is not the one to be removed, set the new current node as the next one
            curr_node = curr_node.next
            # then, increment the value of the i counter by 1
            i += 1

    # method to print the list out
    def print_list(self):
        # first, we create an empty array where we are going to insert all of the node data
        node_list = []

        # then, we set the starting node as the head node
        node = self.head

        # then, we loop as long as node.next exists (loop until end of linked list)
        while node:
            # while this is true:
            # first, add the node data to the node_list
            node_list.append(node.data)
            # then, go to the next node using curr_node.next
            node = node.next

        # finally, after we have added all of the nodes to the node_list, print it out
        print(node_list)


if __name__ == "__main__":
    # create a new linked list object
    linked_list = LinkedList()

    # preform linked list operations
    linked_list.insert(1)
    linked_list.insert_values(["ben", 1000, 10000])
    linked_list.insert_index(2, "new data")

    linked_list.delete_index(1)

    print(linked_list.get_len())

    # output the linked list
    linked_list.print_list()

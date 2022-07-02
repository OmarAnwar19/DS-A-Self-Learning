class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node
        self.tail = new_node

    def insert_values(self, data_list):
        for data in data_list:
            self.insert(data)

    # INSERT AFTER VALUE METHOD
    def insert_after_val(self, ins_val, data):
        # variables so we can loop through the list
        i = 0
        curr_node = self.head

        # a variable for if a match was found, if false at end, return error
        data_found = False

        # while loop is true
        while curr_node:
            # if match found
            if curr_node.data == ins_val:
                # set variable for data found as true
                data_found = True

                # get the next node relative to the current node
                next_node = curr_node.next

                # create new node using data in
                new_node = Node(data, next_node)

                # set the next node of the current node as the new node
                curr_node.next = new_node

                # exit loop
                break

            # if match not found, move to next node
            curr_node = curr_node.next
            i += 1

        # if data_found var is still false, that means no data match found
        if data_found == False:
            # so, return an error
            raise Exception("No node with that value exists.")

    def delete_by_value(self, remove_val):
        # variables so we can loop through the list
        i = 0
        curr_node = self.head

        # a variable for if a match was found, if false at end, return error
        data_found = False

        while curr_node:
            # if the data of the next node is the one to be removed
            if curr_node.next.data == remove_val:
                # set variable for data found as true
                data_found = True

                # link the current node, and the node 2 ahead
                next_node = curr_node.next
                curr_node.next = next_node.next

                # break the loop
                break

            curr_node = curr_node.next
            i += 1

        # if data_found var is still false, that means no data match found
        if data_found == False:
            # so, return an error
            raise Exception("No node with that value exists.")

    def print_list(self):
        node_list = []

        node = self.head

        while node:
            node_list.append(node.data)
            node = node.next

        print(node_list)


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_values([1, 10, 100, 1000, 10000])
    linked_list.insert_after_val(10, 50)

    linked_list.print_list()

    linked_list.delete_by_value(100)

    linked_list.print_list()

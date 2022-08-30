class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_head(self, val):
        self.head = Node(val, self.head)

    def insert(self, val):
        if self.head == None:
            self.insert_head(val)
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        new_node = Node(val)

        curr.next = new_node
        self.tail = new_node

    def insert_values(self, values):
        for val in values:
            self.insert(val)

    def get_len(self):
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next

        return count

    def insert_index(self, index, val):
        if index < 0 or index > self.get_len():
            return -1
        elif index == 0:
            self.insert_head(val)
            return

        i = 0
        curr = self.head

        while curr:
            if i+1 == index:
                next = curr.next
                new = Node(val, next)
                curr.next = new
                break

            curr = curr.next
            i += 1

    def delete_index(self, index):
        if index < 0 or index > self.get_len():
            return -1
        elif index == 0:
            self.head = self.head.next
            return

        i = 0
        curr = self.head

        while curr:
            if i+1 == index:
                next = curr.next
                curr.next = next.next
                break

            curr = curr.next
            i += 1

    def print_list(self):
        r_str = ""
        curr = self.head

        while curr:
            r_str += f"{curr.val} --> "
            curr = curr.next

        print(r_str)


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

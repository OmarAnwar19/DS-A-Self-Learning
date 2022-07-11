class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # to change the search for delete from method 1 to method 2, it is really easy
            # first, we have to find the max_value of the left sub-tree, instead of the min_val of the right sub-tree
            max_val = self.left.find_max()
            # then, we set the current data as the max_val from left sub-tree, instead of the min_val from right sub-tree
            self.data = max_val
            # finally, we set the left sub-tree by recursively calling delete on the left sub-tree this time,
            # we also pass in max_val (instead of calling delete on right sub-tree passinging in min_val)
            self.left = self.left.delete(max_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    arr = [17, 4, 1, 29, 9, 23, 18, 34]
    arr_bst = build_tree(arr)

    print(f"Before Deleting 29: {arr_bst.in_order_traversal()}")
    arr_bst.delete(29)
    print(f"After Deleting 29: {arr_bst.in_order_traversal()}")

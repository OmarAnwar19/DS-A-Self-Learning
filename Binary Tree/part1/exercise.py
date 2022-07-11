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

    def dfs_in_order(self):
        elements = []

        if self.left:
            elements += self.left.dfs_in_order()

        elements.append(self.data)

        if self.right:
            elements += self.right.dfs_in_order()

        return elements

    # same as in order, except elements.append(self.append) is right before return elements
    def dfs_post_order(self):
        elements = []

        if self.left:
            elements += self.left.dfs_in_order()

        if self.right:
            elements += self.right.dfs_in_order()

        elements.append(self.data)

        return elements

    # same as in order, except elements.append(self.append) is the first append we do
    def dfs_pre_order(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.dfs_in_order()

        if self.right:
            elements += self.right.dfs_in_order()

        return elements

    # find min
    def find_min(self):
        # if there is no elements in the left sub-tree, that means we are at the left-most node
        if self.left is None:
            # so, return the data of that node
            return self.data

        # otherwise, recursively call the next level to the left of the current sub-tree
        return self.left.find_min()

    # find max
    def find_max(self):
        # if there is no elements in the right sub-tree, that means we are at the right-most node
        if self.right is None:
            # so, return the data of that node
            return self.data

        # otherwise, recursively call the next level to the right of the current sub-tree
        return self.right.find_max()

    # calculate sum
    def calculate_sum(self):
        # the sum starts as the value of the root node
        sum = self.data

        # then, while there are elements in the left sub-tree
        if self.left:
            # add them to the total sum
            sum += self.left.calculate_sum()

        # same as above, but for the right sub-tree
        if self.right:
            sum += self.right.calculate_sum()

        # then, return the current sum,
        return sum


def build_tree(arr):
    root = BinarySearchTreeNode(arr[0])

    for i in range(1, len(arr)):
        root.add_child(arr[i])

    return root


if __name__ == "__main__":
    arr = [17, 4, 1, 29, 9, 23, 18, 34]
    arr_bst = build_tree(arr)

    print(f"Pre-Order Traversal: {arr_bst.dfs_pre_order()}")
    print(f"In-Order Traversal: {arr_bst.dfs_in_order()}")
    print(f"Post-Order Traversal: {arr_bst.dfs_post_order()}")

    print(f"Min: {arr_bst.find_min()}")
    print(f"Min: {arr_bst.find_max()}")
    print(f"Sum: {arr_bst.calculate_sum()}")

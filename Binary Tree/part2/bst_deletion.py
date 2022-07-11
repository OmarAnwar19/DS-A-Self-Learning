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

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data

        return self.right.find_max()

    # method to delete a value from the binary search tree
    def delete(self, del_val):
        # first, we check if the del_val is greater than the current node data
        if del_val < self.data:
            # if so, we have to traverse the left sub-tree, but first, we make sure it exists
            if self.left:
                # if so, then recursively call delete on the left sub-tree,
                # this will reset this loop, checking if the current value is less, greater, or equal to del_val
                # it will keep calling this loop recursively until the current value is the same as del_val
                # then, we will go to the else condition,
                self.left = self.left.delete(del_val)
        # then, if the value is not less than del_val, we check if it is greater than it
        elif del_val > self.data:
            # if so, we have to traverse the right sub-tree, but first, we make sure it exists
            if self.right:
                # same principal as the recursive call for self.left, but this time for the right side
                self.right = self.right.delete(del_val)
        # otherwise, if left and right are neither larger or smaller, that means the current node is del_val
        else:
            # we first check if we are at the very end of the tree,
            # if there is nothing in the left or right sub-tree, we are at the end of the tree, and value is not in it
            if not self.left and not self.right:
                # so, just return None
                return None

            # otherwise, that means either left or right exists, but we are not sure if both exist

            # if just left exists, that means there is only one child, the right one, so return it
            if self.left is None:
                return self.right

            # if just right exists, that means there is only one child, the left one, so return it
            if self.right is None:
                return self.left

            # if both the left and right sub-trees exist, that means we have two child nodes to delete

            # as we remember, we do this by finding the minimum value from the right sub-tree, make it the parent node, then delete the duplicate node
            # so, find the min_val from the right sub-tree
            min_val = self.right.find_min()
            # then, set the current node value (the one to be deleted) as the min_val from the right sub-tree
            self.data = min_val
            # finally, delete the duplicate node, by recursively calling the delete function on the right sub-tree
            # --> this will keep checking the right side, until it finds min_val in it
            # --> then, will replace it with its own min val, and keep repeating these two operations
            # --> finally, when no right elements exist, it will return the final right sub-tree, which we assign to the current right sub-tree
            self.right = self.right.delete(min_val)

        # return the current self node, so that we move over in the binary search tree while doing our recursive calls,
        # if there are no recursive calls, then it will delete the final BST, with the del_val removed
        return self


def build_tree(arr):
    root = BinarySearchTreeNode(arr[0])

    for i in range(1, len(arr)):
        root.add_child(arr[i])

    return root


if __name__ == "__main__":
    # array for an example of build_tree
    arr = [17, 4, 1, 29, 9, 23, 18, 34]
    # create a binary search tree by calling build_tree, passing in our array above
    arr_bst = build_tree(arr)

    # print the binary search tree before deleting 29
    print(f"Before Deleting 29: {arr_bst.dfs_in_order()}")

    # call the method to delete 29 from the binary search tree
    arr_bst.delete(29)

    # print the binary search tree after deleting 29
    print(f"After Deleting 29: {arr_bst.dfs_in_order()}")

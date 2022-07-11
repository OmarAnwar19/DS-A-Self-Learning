# the class for each node in our binary search tree
class BinarySearchTreeNode:
    # this is practically the same as our general tree, except we only have left and right child-nodes
    def __init__(self, data) -> None:
        # the data is passed in
        self.data = data
        # the left and right child-nodes start out as None
        self.left = None
        self.right = None

    # add child method
    def add_child(self, data):
        # first thing, since a BST can not have duplicated,
        # if the child already exists, do not add it again
        if data == self.data:
            return

        # if the new child's data is less than the current node's data,
        # add it to the left of the current node
        if data < self.data:
            # first, we have to check if the current node has anything in its left sub-tree
            # if it does have something to its left,
            if self.left:
                # we recursively call add_Child on self.left;
                # this will keep checking this loop, until it gets to a point where self.left does not exist,
                # at that point, it will create the new node and add it to the proper sub-tree
                self.left.add_child(data)
            # if not, add a new node with this data to a new left sub-tree
            else:
                # create new BSTNode, and add it to the self.left, creating a new sub-tree
                self.left = BinarySearchTreeNode(data)

        # if the new child's data is greater than the current node's data,
        # add it to the right of the current node
        if data > self.data:
            # this is the exact same code as above for the left, except self.left is swapped with self.right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # dfs_in_order method, traverses through the BFS using depth-first-serach in order
    def dfs_in_order(self):
        # create an empty array, which will hold the in order traversed binary search tree
        elements = []

        # * as we know, with in order traversal, you navigate through the left sub-tree,
        # * then the root node, then the right sub-tree
        # * --> this is what we will do here

        #! start at root node, then go to left node. Then, you add the root node, then add the right node
        #! --> then, recursive call is made, to you go one step deeper into the left sub-tree,
        #!     then, you add its root node, then its right sub-tree, and keep doing this until the entire left sub-tree is added
        #! then, you add the root node of the entire tree, and repeat the proccess we did on the left sub-tree on right sub-tree

        # first, while there is an element in the left sub-tree
        if self.left:
            # since the dfs_in_order method returns an array,
            # you recursively call dfs_in_order on the left side, which will add any left elements into a new array,
            # then, this array will be added to our original elements array after the recursion is done
            # therefore, we will have added all of the left sub-tree elements to our original array
            elements += self.left.dfs_in_order()

        # then, add the root node data to the elements array
        elements.append(self.data)

        # then, while there are elements in the right sub-tree, add them to our elements array
        if self.right:
            elements += self.right.dfs_in_order()

        # finally, return the now populated array
        return elements

    # method to search for a value in the binary search tree
    def search(self, search_val):
        # first, check if the current root node is the search_val,
        if self.data == search_val:
            # if so, then just return True, because it has been found
            return True

        # if its not the root node, we actually have to search for it,
        # if the search_value is less than the root node, that means it is in the left sub-tree
        if search_val < self.data:
            # we have to check while there are any elements in the left sub-tree,
            if self.left:
                # if there are elements, we will recursively call search on the left sub tree, passing in our search_val
                # this will go into the next level of the left sub-tree, and check if the current root data is the search_val,
                # if it is, it will return it, otherwise, it will call recursively again, as long as left sub-tree still exists
                self.left.search(search_val)
            # if not, that means we have reached the end of the tree, and the value has not been found,
            else:
                # so, we can confidently return false
                return False

        # otherwise, if the search_value is greater than the root node, that means it is in the right sub-tree
        if search_val > self.data:
            # same as the left sub-tree above, but for the right sub-tree search,
            # simply, all of the self.left are swapped for self.right
            if self.right:
                self.right.search(search_val)
            else:
                return False


# helper method to build our Binary Search Tree
def build_tree(arr):
    # first, we create our root node by making a new BinarySearchTreeNode,
    # --> with the data in our first element in the array
    root = BinarySearchTreeNode(arr[0])

    # then, we loop through each element after the first one in our array,
    for i in range(1, len(arr)):
        # then, add it as a child to our root node we created above
        root.add_child(arr[i])

    # finally, return the root node, which contains the entire tree
    return root


if __name__ == "__main__":
    # array for an example of build_tree
    arr = [17, 4, 1, 29, 9, 23, 18, 34]

    # create a binary search tree by calling build_tree, passing in our array above
    arr_bst = build_tree(arr)

    # print the array by traversing through it, then printing the final returned elements array
    print(arr_bst.dfs_in_order())

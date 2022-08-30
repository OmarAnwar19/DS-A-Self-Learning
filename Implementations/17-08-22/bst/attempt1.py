class BSTNode:
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
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

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

    def dfs(self):
        elements = []
        if self.left:
            elements += self.left.dfs()

        elements.append(self.data)

        if self.right:
            elements += self.right.dfs()

        return elements

    def delete(self, del_val):
        if del_val < self.data:
            if self.left:
                self.left = self.left.delete(del_val)
        elif del_val > self.data:
            if self.right:
                self.right = self.right.delete(del_val)
        else:
            if not self.left and not self.right:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(arr):
    root = BSTNode(arr[0])

    for i in range(1, len(arr)):
        root.add_child(arr[i])

    return root


if __name__ == "__main__":
    arr = [17, 4, 1, 29, 9, 23, 18, 34]
    arr_bst = build_tree(arr)

    print(f"Before Deleting 29: {arr_bst.dfs()}")
    arr_bst.delete(29)
    print(f"After Deleting 29: {arr_bst.dfs()}")

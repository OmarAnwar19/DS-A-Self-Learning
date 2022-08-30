class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if child == self.data:
            return

        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = BSTNode(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BSTNode(child)

    def search(self, search_val):
        if search_val == self.data:
            return True

        if search_val < self.data:
            if self.left:
                self.left.search(search_val)
            else:
                return False
        else:
            if self.right:
                self.right.search(search_val)
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

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

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

            if not self.left:
                return self.right

            if not self.right:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


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

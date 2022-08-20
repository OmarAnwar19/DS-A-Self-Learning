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

    
    def bfs(self):
      #We first initialise a queue with a single node: the root of the tree
      queue = [self.val]
      #we also create an empty array for the values of the tree
      elements = []

      #while there are elements in the queue
      while queue:
        #Dequeue the first node
        currentNode = queue.pop(0)
        #Read the node value, and add it to our values array
        elements.append(currentNode.value)

        #Enqueue child nodes (if any)
        if currentNode.left!=None:
          #Enqueue the left node at the end of the queue:
          queue.append(currentNode.left)
        if currentNode.right!=None:
          #Enqueue the right node at the end of the queue:
          queue.append(currentNode.right)

        #return the values array  
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

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            
        return self


def build_tree(arr):
    root = BinarySearchTreeNode(arr[0])

    for i in range(1, len(arr)):
        root.add_child(arr[i])

    return root


if __name__ == "__main__":
    # array for an example of build_tree
    arr = [17, 4, 1, 29, 9, 23, 18, 34]
    arr_bst = build_tree(arr)

    print(f"Before Deleting 29: {arr_bst.bfs()}")
    arr_bst.delete(29)
    print(f"After Deleting 29: {arr_bst.bfs()}")

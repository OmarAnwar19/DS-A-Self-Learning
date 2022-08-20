def bfs(self):
  #We first initialise a queue with a single node: the root of the tree
  queue = [tree]
  #we also create an empty array for the values of the tree
  values = []

  #while there are elements in the queue
  while queue:
    #Dequeue the first node
    currentNode = queue.pop(0)
    #Read the node value, and add it to our values array
    values.append(currentNode.value)

    #Enqueue child nodes (if any)
    if currentNode.left!=None:
      #Enqueue the left node at the end of the queue:
      queue.append(currentNode.left)
    if currentNode.right!=None:
      #Enqueue the right node at the end of the queue:
      queue.append(currentNode.right)
      
    #return the values array  
    return values

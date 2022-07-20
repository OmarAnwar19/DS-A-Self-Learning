# Depth First Search and Breadth First Search

---

## What is BFS?

BFS is an algorithm that is used to graph data or searching tree or traversing structures. The algorithm efficiently visits and marks all the key nodes in a graph in an accurate breadthwise fashion.

This algorithm selects a single node (initial or source point) in a graph and then visits all the nodes adjacent to the selected node. Once the algorithm visits and marks the starting node, then it moves towards the nearest unvisited nodes and analyses them.

Once visited, all nodes are marked. These iterations continue until all the nodes of the graph have been successfully visited and marked. The full form of BFS is the Breadth-first search.

To sum up the logic, the BFS Algorithm steps look like this:

    1. Add the root/start node to the Queue.
    2. For every node, set that they don't have a defined parent node.
    3. Until the Queue is empty:
        - Extract the node from the beginning of the Queue.
        - Perform output processing.
        - For every neighbor of the current node that doesn't have a defined parent (is not visited), add it to the Queue, and set the current node as their parent.

### When to use BFS?

Breadth First Search is generally the best approach when the depth of the tree can vary, and you only need to search part of the tree for a solution. For example, finding the shortest path from a starting value to a final value is a good place to use BFS.

---

## What is DFS?

DFS is an algorithm for finding or traversing graphs or trees in depth-ward direction. The execution of the algorithm begins at the root node and explores each branch before backtracking. It uses a stack data structure to remember, to get the subsequent vertex, and to start a search, whenever a dead-end appears in any iteration. The full form of DFS is Depth-first search.

The DFS algorithm is pretty simple and consists of the following steps: 1. Mark the current node as visited. 2. Traverse the neighboring nodes that aren't visited and recursively call the DFS function for that node.

The algorithm starts at the root (top) node of a tree and goes as far as it can down a given branch (path), then backtracks until it finds an unexplored path, and then explores it. It preforms this recursively, by going to a node, then checking all of its left sub-tree elements, then all of its right sub-tree elements, and then repeating this proccess until the entire tree is explored.

### When to use DFS?

Depth First Search is commonly used when you need to search the entire tree. It's easier to implement (using recursion) than BFS, and requires less state: While BFS requires you store the entire 'frontier', DFS only requires you store the list of parent nodes of the current element.

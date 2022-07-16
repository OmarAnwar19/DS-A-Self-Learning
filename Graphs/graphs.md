# Graphs

_great_resource: https://www.baeldung.com/cs/adjacency-matrix-list-complexity_

## What are they?

A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph.

An example is that of a network on Facebook. You, and each of your friends, are individual nodes, and then when you connect as friends, an edge forms between your two profile nodes. Then, as you connect to more friends, and your friends connect to other people aswell, the network keeps expanding, and nodes keep getting connected together with edges, with no maximum number of connections to a specific friend.

## What are they used for?

Graphs are used to solve many real-life problems. Graphs are used to represent networks. The networks may include paths in a city or telephone network or circuit network. Graphs are also used in social networks like linkedIn, Facebook. For example, in Facebook, each person is represented with a vertex(or node). Each node is a structure and contains information like person id, name, gender, locale etc.

### Directed vs Undirected Graph

The main difference between directed and undirected graph is that a directed graph contains an ordered pair of nodes whereas an undirected graph contains an unordered pair of nodes. A directed graph will have a node point towards another node, while an unorded graph will not have any nodes explicitly pointing towards eachother.

### Weighted vs Un-weighted Graph

If edges in your graph have weights then your graph is said to be a weighted graph, if the edges do not have weights, the graph is said to be unweighted. A weight is a numerical value attached to each individual edge.

For example, in a flight booking website, if you want to navigate from point a to point d, there may be two different paths; points: a --> b --> c --> d OR points: a --> c --> d. Although the second path might seem shorter, if they have weights attached to them, the first path might actually be shorter, if the weights between the paths (weight here is the distance) is less than the weights in the second path.

### Graph vs Tree

Although they may seem simillar, the main difference between a graph and a tree is that in a tree there is only one path between any two nodes, while in a graph, each node may have any number of edges connecting them. In reality, a tree is a specialized version of a graph.

---

## Implementation

The two main methods to store a graph in memory are adjacency matrix and adjacency list representation.

---

### Adjacency Matrix

The first way to represent a graph in a computer’s memory is to build an adjacency matrix. Assume our graph consists of n nodes numbered from 1 to n. An adjacency matrix is a binary matrix of size n \times n. There are two possible values in each cell of the matrix: 0 and 1. Suppose there exists an edge between nodes n*{i} and n*{j}. It means, that the value in the i^{th} row and j^{th} column of such matrix is equal to 1. Importantly, if the graph is undirected then the matrix is symmetric.

#### Big O Complexity - time:

Assuming the graph has n nodes, the time complexity to build such a matrix is O(n^2). To fill every value of the matrix we need to check if there is an edge between every pair (n*{i}, n*{j}) of nodes. That is why the time complexity of building the matrix is O(n^2).

#### Big O Complexity - space :

The space complexity is also O(n^2). Given a graph, to build the adjacency matrix, we need to create a square n \* n matrix and fill its values with 0 and 1; this costs us O(n^2) space.

---

### Adjacency List

The other way to represent a graph in memory is by building the adjacent list. If the graph consists of n nodes, then the list L contains n elements. Each element L*{i} is also a list and contains all the nodes, adjacent to the current vertex v*{i}. By choosing an adjacency list as a way to store the graph in memory, this may save us space. i.e we create a dictionary, where each key is the node, and each value is a list of all its adjascent nodes.

#### Big O Complexity - time:

If m is the number of edges in a graph, then the time complexity of building such a list is O(m).

#### Big O Complexity - space :

The space complexity is O(n + m). But, in the worst case of a complete graph, the time and space complexities reduce to O(n^2).

---

### Pros and Cons

**_Adjacency Matrix_**

**The main advantage of such representation is that we can check in O(1) time if there exists edge e*{ij} = (v*{i}, v\_{j})} by simply checking the value at i^{th} row and j^{th} column of our matrix.**

    - Uses O(n^2) memory
    - It is fast to lookup and check for presence or absence of a specific edge
    - between any two nodes O(1)
    - It is slow to iterate over all edges
    - It is slow to add/delete a node; a complex operation O(n^2)
    - It is fast to add a new edge O(1)

**_Adjacency List_**

**This representation is much more efficient if space matters.**

    - Memory usage depends more on the number of edges (and less on the number of nodes),
    - which might save a lot of memory if the adjacency matrix is sparse
    - Finding the presence or absence of specific edge between any two nodes
    - is slightly slower than with the matrix O(k); where k is the number of neighbors nodes
    - It is fast to iterate over all edges because you can access any node neighbors directly
    - It is fast to add/delete a node; easier than the matrix representation
    - It fast to add a new edge O(1)

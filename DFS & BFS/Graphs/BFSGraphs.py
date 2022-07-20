# first, since BFS uses a queue to keep track of visited nodes, we have to import it
from collections import deque


# simple implementation of a graph to wrap our bfs
class Graph:
    # Constructor
    def __init__(self):
        self.adj_list = {
            "A": ["B", "D"],
            "B": ["A", "C"],
            "C": ["B"],
            "D": ["A", "E", "F"],
            "E": ["D", "F", "G"],
            "F": ["D", "E", "H"],
            "G": ["E", "H"],
            "H": ["G", "F"]
        }

    # Add edge to the graph
    def add_edge(self, key, value):
        if key in self.adj_list:
            self.adj_list[key].append(value)
        else:
            self.adj_list[key] = [value]

    # Print the graph representation
    def print_adj_list(self):
        for key in self.adj_list.keys():
            print(f"node {key}: {self.adj_list[key]}")

    # the actual function to preform breadth first search
    # we take in self, and the node we are looking for
    def bfs(self, start_node, target_node):
        # we first check if the start or target node are actually even part of the graph
        if start_node not in self.adj_list or target_node not in self.adj_list:
            # if they are not (not in adjacency list), we return False before we check anything
            return False

        # as we know, we have to keep track of visited nodes, to prevent infinite loops
        visited = []
        # then, we create a queue, which adds all of the nodes, and then checks them top down
        # --> this ensures that we check nodes in the order in which they appear in the graph (breadth first)
        queue = deque()

        # we have to save the parent nodes, for when we re-structure the path
        # once we get to the target_node, we will keep looping through each parent node while not None,
        # we will add each of them to the path, until parent is None, then we have re-structured the whole path
        parent = {}
        # since the parent node of the start node is None, we add that to the dictionary
        parent[start_node] = None

        # Next, what we do is add the start node to the queue, and to the visited list
        queue.appendleft(start_node)
        visited.append(start_node)

        # Finally, we create a path_found variable, and set it to False
        # if we find a path, this becomes true, and we re-construct the path
        path_found = False

        # * now, we have done everything specific to the start node, and can start finding the path to target_node

        # we keep looping while the queue is not empty
        # we are going to keep adding adjacent nodes to the queue until there are no more edges
        while not len(queue) == 0:
            # the first thing we do is pop the top node from the queue
            current_node = queue.popleft()

            # then, we check if the current node is the target node
            # --> if it is, that means we have found our node, and found a path from start to target node
            if current_node == target_node:
                # so, set path_found to true, and break the loop
                path_found = True
                break

            # then, if the current node is not the target one, that means we are in the middle of traversing the adj list
            # so, loop over each node which is adjacent to the current node
            for next_node in self.adj_list[current_node]:
                # if that node has not already been visited,
                # --> (if it has, that means its already accounted for, so we dont do anything to it to avoid infinite loop)
                if next_node not in visited:
                    # we add it to the queue
                    queue.appendleft(next_node)
                    # add its parent to the parent node dictionary (so we can reconstruct a path if it applies)
                    parent[next_node] = current_node
                    # then, we add it to the visited nodes array
                    visited.append(next_node)

                # we keep repeating this proccess, until we have added each adjacent node to the queue, and note their parents
                # then, we check each adjacent node from those, and add any of their adjacent nodes to the queue
                # once the current node does not have any more adjacent nodes, or all of its adjacent nodes have already been visited,
                # we exit the loop, and we re-construct the path

                # --> we do this by creating the path backwards, by appending the target node, and then appending its parent node to the path
                # then, we keep appending each of their parent nodes, and this means that we ignore any non-parent nodes, and add releavnt ones
                # everntually, we reach the start node, which has no parents, and we have reconstructed the path
                # so, we reverse it, since it was created backwards, and return it

        # Path reconstruction
        # first, create an empty path,
        path = []
        # if path found is true, we reconstruct it, if not, this empty path is returned as is
        if path_found:
            # if the path is found, we re-create it backwards, and start by appending target_node
            path.append(target_node)
            # so, we loop while the current node's parent is not none (until we reach start node)
            while parent[target_node] is not None:
                # then, we apprend the parent of the current node (since this is part of the correct path)
                path.append(parent[target_node])
                # and, we set the target node as the parent
                target_node = parent[target_node]

                # then, we check its parent, and add it to the path, then set that parent to the target node,
                # and we repeat until the parent of the current node is None, when we have reached the start node

            # once parent is none (at start node), we reverse the path (since we started from target backwards)
            path.reverse()

        # finally, we return the path, which is either a blank array if no path_found, or a re-constructed array if found
        return path


if __name__ == "__main__":
    # an example of a graph implemented as an adjacency list
    # we have a dictionary, with each node as keys, and then its adjacent nodes as values
    abc_graph = Graph()

    print(f"path: {abc_graph.bfs('A', 'G')}")

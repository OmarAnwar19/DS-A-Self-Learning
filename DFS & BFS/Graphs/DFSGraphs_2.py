# simple implementation of a graph to wrap our dfs
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

    # the actual function to preform depth first search
    # we take in self, and the node we are looking for

    # we also pass in a path, and visited nodes arrays,
    # path keeps track of the path from start_node to target_node,
    # and visited keeps track of all of the nodes we visited, to avoid an infinite loop
    def dfs(self, start_node, target_node, path=[], visited=[]):
        if start_node not in self.adj_list or target_node not in self.adj_list:
            # if they are not (not in adjacency list), we return False before we check anything
            return False

        # we start by appending the start node to both the path, and the visited nodes arrays
        # appending start_node to path adds it to the path from start to target,
        # and appending it to visited stops us getting into a loop where we check it over and over

        # as this function is called recursively, we append the new start_node, which is the neighbours of this node
        path.append(start_node)
        visited.append(start_node)

        # afterwards, we check if the current node is the target node,
        # this occurs if start and target are same, or, if we have traversed to the target node
        if start_node == target_node:
            # if this is the case, we return the path
            return path

        # then, we loop for every node that is adjacent to the current node (in adjacency list)
        for next_node in self.adj_list[start_node]:
            # if the node has not already been visited (not in visited)
            if next_node not in visited:
                # then, you recursively call the funciton to find the path from the next_node, to the start_node
                # by doing this for every edge of the original start node, we find paths from each edge to each start,
                # then, we take all of the connections from neighbour to start, and attach them together to create a full path
                result = self.dfs(next_node, target_node, path, visited)

                if result is not None:
                    # return the result
                    return result

        # if the loop above is exited, that means the current node is not part of the path,
        # so, remove it from the top of the path array
        path.pop()

        # if no path is found, return None
        return None


if __name__ == "__main__":
    # an example of a graph implemented as an adjacency list
    # we have a dictionary, with each node as keys, and then its adjacent nodes as values
    abc_graph = Graph()

    print(f"path: {abc_graph.dfs('A', 'F')}")

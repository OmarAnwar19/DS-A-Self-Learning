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

    # function to get all of the paths between a start and end node
    # --> also takes in the current path recursively
    def get_all_paths(self, start, end, path=[]):
        #!!to get all of the paths from point a to c, we have to find all the paths form point b to c, then add point a to all of them!!
        #!! --> this is the principal we will work on to find our paths

        # we create path. this is the pre-existing path, + the current start location
        path = path + [start]

        # the first thing we check is if the start is even a correct location
        if start not in self.adj_list:
            # if not, return an empty array, since there are no paths originating from it
            return []

        # then, we check if the start and end are same
        # --> this is also used in our recursive call, as since we move our start locaiton each time, eventually start will be our end locaiton
        # at that point, we hit this if statement, which will return our final path
        if start == end:
            # if they are, dont check any paths, just return the current path (same location)
            return [path]

        # this variable will hold all of the possible paths we get by traversing through each edge from our start
        all_paths = []

        # otherwise, that means the locations are both routable
        # loop over each edge which connects to our start location in our adj_list
        for location in self.adj_list[start]:
            # if the location is not already in path (we have not already traversed to it)
            if location not in path:
                # get all of the possible paths from that path (the one that connects to our start), to the end location
                new_paths = self.get_all_paths(location, end, path)

                # loop over each one of the new paths, and add them to our all_paths
                for p in new_paths:
                    # add each individual path to all_paths
                    all_paths.append(p)

        # finally, return all of the paths from location start to end
        return all_paths

    # function to get the shortest path between start and end based on lowest number of stops
    def get_shortest_path(self, start, end, path=[]):
        # we create path. this is the pre-existing path, + the current start location
        path = path + [start]

        # the first thing we check is if the start is even a correct location
        if start not in self.adj_list:
            # if not, return an empty array, since there are no paths originating from it
            return []

        # then, we check if the start and end are same
        # --> this is also used in our recursive call, as since we move our start locaiton each time, eventually start will be our end locaiton
        # at that point, we hit this if statement, which will return our final path
        if start == end:
            # if they are, dont check any paths, just return the current path (same location)
            return path

        # set a variable for the current shortest path, starts as none
        shortest_path = None

        # the first part of this loop is the same as the one in get_all_paths
        for location in self.adj_list[start]:
            if location not in path:
                # here is where it changes, so, we get the current path
                curr_path = self.get_shortest_path(location, end, path)

                # then, if is valud
                if curr_path:
                    # we have to check whether or not we should set it as the shortest path
                    # we set it as the shortest path under two conditions:
                    # if the current shortest path is None (has nto been set yet)
                    # or, if it is shorter than the current shortest path
                    if shortest_path is None or len(curr_path) < len(shortest_path):
                        shortest_path = curr_path

        # finally, return the shortest path
        return shortest_path


if __name__ == "__main__":
    # an example of a graph implemented as an adjacency list
    # we have a dictionary, with each node as keys, and then its adjacent nodes as values
    abc_graph = Graph()

    print(f"path: {abc_graph.dfs('A', 'F')}")

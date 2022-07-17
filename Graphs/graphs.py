# graph class
class Graph:
    # init takes in our edges array, which will be transformed into an adjacency list
    def __init__(self, edges):
        # edges, in array form
        self.edges = edges
        # internal graph_dict (our adjacency list), starts as blank
        self.graph_dict = {}

        # call the internal method to transform our edges into an adjacency list
        self.__make_adj_list()

    # helper function to transform a array of edge tuples into a adjacency dictionary
    def __make_adj_list(self):
        # loop over key and value in each edges tuple
        for key, value in self.edges:
            # if the key is already in the internal dictionary:
            if key in self.graph_dict:
                # append the current value to the dictionary array at that key value
                self.graph_dict[key].append(value)
            # otherwise, if the key is not in the internal dictionary
            else:
                # create a new entry in the dictionary with the current key and value
                self.graph_dict[key] = [value]

    # function to get all of the paths between a start and end node
    # --> also takes in the current path recursively
    def get_all_paths(self, start, end, path=[]):
        #!!to get all of the paths from point a to c, we have to find all the paths form point b to c, then add point a to all of them!!
        #!! --> this is the principal we will work on to find our paths

        # we create path. this is the pre-existing path, + the current start location
        path = path + [start]

        # the first thing we check is if the start is even a correct location
        if start not in self.graph_dict:
            # if not, return an empty array, since there are no paths originating from it
            return []

        # if thats all good, we can start looking for paths,

        # then, we check if the start and end are same
        # --> this is also used in our recursive call, as since we move our start locaiton each time, eventually start will be our end locaiton
        # at that point, we hit this if statement, which will return our final path
        if start == end:
            # if they are, dont check any paths, just return the current path (same location)
            return path

        # this variable will hold all of the possible paths we get by traversing through each edge from our start
        all_paths = []

        # otherwise, that means the locations are both routable
        # loop over each edge which connects to our start location in our graph_dict
        for location in self.graph_dict[start]:
            # if the location is not already in path (we have not already traversed to it)
            if location not in path:
                # get all of the possible paths from that path (the one that connects to our start), to the end location
                new_paths = self.get_all_paths(location, end, path)

                # * what happens is that we get our initial start location, and add it to our path array,
                # * then, we loop over all of the locations that connect to that initial start location
                # * then, we add them to our path
                # * then, we loop over all of the locations that connect to that location,
                # * we keep doing this, until the current location is the same as our end location,
                # * at this point, that means we have found the path from start to end,
                # * --> and each step of the way, we appended the current location to our path
                # * so now, since start == end, we return path, which is actually the final path from our initial start to our end

                # * this then exits our recursive call, and returns a new path, which we then append to all paths,
                # * when we return all paths now, it has each individual path from start to end

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
        if start not in self.graph_dict:
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
        for location in self.graph_dict[start]:
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
    # an array of all the possible routes in india
    routes = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    # we can create a new graph, with edges as the routes above un-changed
    # however, this proccess is too space-exhaustive, as we have to check each list each time we navigate

    # instead, we can implement an adjacency list using a dictionary
    # our Graph class will transform an array of edges into a adjascency list
    route_graph = Graph(routes)

    # set our current start and end location
    start = "Mumbai"
    end = "Bangaluru"

    # print all the paths between start and end
    print(
        f"Paths from {start} to {end}: {route_graph.get_all_paths(start, end)}")

    # print the shortest path between start and end
    print(
        f"Shortest path from {start} to {end}: {route_graph.get_shortest_path(start, end)}")

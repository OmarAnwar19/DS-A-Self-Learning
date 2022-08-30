class Node:
    def __init__(self, data: str = None, parent: "Node" = None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def add_children(self, arr):
        for child in arr:
            self.children.append(child)
            child.parent = self

    def get_level(self):
        curr = self.parent
        level = 0

        while curr:
            level += 1
            curr = curr.parent

        return level

    def print_tree(self):
        level = self.get_level()
        prefix = " " * level * 5

        print(f"{prefix} |__ {self.data}")

        if self.children:
            for child in self.children:
                child.print_tree()


if __name__ == "__main__":
    root = Node("root")

    sub_level1 = Node("sub_level1", root)
    sub_level2 = Node("sub_level2")

    root.add_child(sub_level1)
    root.add_child(sub_level2)

    sl1_child1 = Node("sub_level1_child1")
    sl1_child2 = Node("sub_level1_child2")
    sl1_child3 = Node("sub_level1_child3")

    sub_level1.add_children([sl1_child1, sl1_child2, sl1_child3])

    sl2_child1 = Node("sub_level1_child1", sub_level2)
    sl2_child2 = Node("sub_level1_child2", sub_level2)
    sl2_child3 = Node("sub_level1_child3", sub_level2)

    root.print_tree()

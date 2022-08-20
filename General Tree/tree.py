# we can create a general tree class, to represent this data structure


# first step is to create a TreeNode class to represent each node in the tree
class TreeNode:
    # the node takes in data, child nodes, and a parent node
    def __init__(self, data=None) -> None:
        self.data = data
        # the child nodes is just an empty array, which we will store the children in later
        self.children = []
        # the parent node will be set on child node creation, so starts out as None
        self.parent = None

    # method to add children to the tree node (append children to its array)
    # we call this method on the parent node, so it sets the parent of each child node as itself (as it is called on parent node)
    def add_child(self, child):
        # first, we have to set the parent of the child node as the current node
        # --> i.e since this is a child, its parent is this one since its direcly above
        child.parent = self

        # append the child to the children array
        self.children.append(child)

    # function to get the level of the current child node
    def get_level(self):
        # this function pretty much just needs to count the number of ancestors for each child node

        # so, start by initializing level as 0
        level = 0
        # then, set the first parent as the parent of the current node
        curr_parent = self.parent

        # then, while the parent node has its own parent node,
        while curr_parent:
            # increment the level by 1,
            level += 1
            # set the curr_parent as the parent of the current node's parent
            curr_parent = curr_parent.parent

        # then, return the level
        return level

    # function to print the tree
    def print_tree(self):
        # first thing we have to do is get the level of the current node
        level = self.get_level()
        # then, create the prefix of the current data by multiplying level * spaces
        prefix = " " * level * 5

        # first, print the data of the root node
        print(f"{prefix} |__ {self.data}")

        # then, for every child node, if they have child nodes of their own
        if self.children:
            # loop over the child nodes, and call their print tree function,
            for child in self.children:
                # this calls the print_tree() function of each child, which prints self.data
                # --> based on which level you are in the tree, it appends n amount of spaces before the print
                child.print_tree()


def build_electronics_tree():
    # so, we first create the parent node
    root = TreeNode(data="Electronics")

    # then, create the child nodes

    # for example, laptop node, child of root node
    laptop = TreeNode(data="Laptop")
    # then, that child node has its own child nodes
    # so, add each child node to its parent node
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    # same thing, but will cell phones
    cellphone = TreeNode(data="Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    # same thing but with tv's
    tv = TreeNode(data="TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("LG"))

    # then, we have to add the main category child nodes as such to the root node
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # finally, after we build the tree, return the root (contains entire tree)
    return root


if __name__ == "__main__":
    # call the build_electronics_tree function to create an electronics tree, return the root node
    electronicsRoot = build_electronics_tree()

    electronicsRoot.print_tree()

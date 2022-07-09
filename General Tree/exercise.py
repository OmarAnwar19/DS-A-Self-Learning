class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    # modifed print function
    def print_tree(self, filter, max_level):
        # first, get the current level to compare it to max_level
        level = self.get_level()

        # if the level < max_level, print the data
        if level < max_level:
            # create the data to be printed, starts as none
            data = None

            # if the filter is name, data is self.name
            if filter == "name":
                data = self.name
            # if the filter is designation, data is self.designation
            elif filter == "designation":
                data = self.designation
            # otherwise, the filter is both, so data is name and designation
            else:
                data = f"{self.name} ({self.designation})"

            spaces = ' ' * level * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + data)

            if self.children:
                for child in self.children:
                    child.print_tree(filter, max_level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_company_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    root.add_child(cto)

    app_head = TreeNode("Aamir", "Application Head")
    infa_head = TreeNode("Vishwa", "Infastructure")

    cto.add_child(app_head)
    cto.add_child(infa_head)

    infa_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infa_head.add_child(TreeNode("Abhijit", "App Manager"))

    hr_head = TreeNode("Gels", "HR Head")
    root.add_child(hr_head)

    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    return root


if __name__ == '__main__':
    comp_tree = build_company_tree()
    comp_tree.print_tree("designation", 1)

from state_space_base.node import Node


class Solution:
    def __init__(self, node: Node):
        """
        :param node: correctly constructs a solution for a problem from a node
        """
        self.node = node
        self.cost = node.cost
        self.solution_path = self.recursive_solution_builder(self.node)

    def recursive_solution_builder(self, node: Node) -> [Node]:
        if node.parent is None:
            return [node]

        path = self.recursive_solution_builder(node.parent)
        path.append(node)
        return path

    def __str__(self):
        string = ''
        for node in self.solution_path:
            if node.prev_action is not None:
                string += str(node.prev_action) + '\n'
            string += str(node.state) + '\n'
        return string

    def __eq__(self, other):
        return self.__str__() == str(other)

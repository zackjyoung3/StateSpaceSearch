from node import Node


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
        for node in self.solution_path:
            if node.prev_action is not None:
                print(node.prev_action)
            print(node)

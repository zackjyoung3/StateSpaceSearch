from state import State
from action import Action
from typing import Type


class Node:
    def __init__(self, s: State, node: 'Node', action: Action, cost: float, func_measure: float):
        """
        :param s: the state that the node is associated with
        :param node: the parent of this node
        :param action: the action that was taken to obtain the state that is associated with this node
        :param cost: the cost that it took to get to this node i.e. accumulated cost
        :param func_measure: the heuristic evaluation function measure for this node (if UCS just cost)
        """
        self.s = s
        self.parent = node
        self.prev_action = action
        self.cost = cost
        self.func_measure = func_measure

    def __lt__(self, other):
        return self.func_measure < other.func_measure

    def __eq__(self, other):
        return self.func_measure == other.func_measure

    def __hash__(self):
        return hash(self.func_measure)



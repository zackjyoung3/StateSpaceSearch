from abc import ABC
from state_space_base.problem import Problem
from state_space_base.evaluation_function import EvaluationFunction, CostFunction, AStarEval
from priority_queue.priority_queue import MinPriorityQueue
from state_space_base.node import Node
from solution import Solution


class Search(ABC):
    evaluation_function: EvaluationFunction

    def __init__(self, problem: Problem):
        self.problem = problem

    def search(self, problem: Problem = None) -> Solution:
        self.problem = problem if problem is not None else self.problem
        reached = {}
        frontier = MinPriorityQueue()
        node = Node(self.problem.get_initial_state(), None, None, 0, 0)
        frontier.enqueue(node)
        reached[node.state] = node
        while not frontier.is_empty():
            node = frontier.dequeue()
            if self.problem.is_goal_state(node.state):
                return Solution(node)
            for action in self.problem.get_actions(node.state):
                s = self.problem.get_result(node.state, action)
                cost = node.cost + self.problem.get_action_cost(node.state, action)
                function_measure = self.evaluation_function.evaluate(s, cost)
                if s not in reached or function_measure < reached[s].func_measure:
                    child = Node(s, node, action, cost, function_measure)
                    reached[s] = child
                    frontier.enqueue(child)
        return None


class UCS(Search):
    def __init__(self, problem: Problem):
        self.evaluation_function = CostFunction()
        super().__init__(problem)


class GBFS(Search):
    def __init__(self, problem: Problem):
        self.evaluation_function = problem.heuristic_eval
        super().__init__(problem)


class AStar(Search):
    def __init__(self, problem: Problem):
        self.evaluation_function = AStarEval(problem.heuristic_eval)
        super().__init__(problem)

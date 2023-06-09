from abc import ABC, abstractmethod
from problem import Problem
from evaluation_function import EvaluationFunction, CostFunction, AStarEval
from priority_queue import MinPriorityQueue
from node import Node
from solution import Solution


class Search(ABC):
    evaluation_function: EvaluationFunction

    def __init__(self, problem: Problem):
        self.problem = problem

    def search(self, problem: Problem) -> Solution:
        reached = {}
        frontier = MinPriorityQueue()
        node = Node(self.problem.get_initial_state(), None, None, 0, 0)
        frontier.enqueue(node)
        reached[node.state] = node
        while not frontier.is_empty():
            node = frontier.dequeue()
            if problem.is_goal_state(node.state):
                return Solution(node)
            for action in problem.get_actions(node.state):
                s = problem.get_result(node.state, action)
                cost = node.cost + problem.get_action_cost(node.state, action)
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

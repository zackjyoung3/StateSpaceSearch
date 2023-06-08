from abc import ABC, abstractmethod
from problem import Problem
from evaluation_function import EvaluationFunction, CostFunction, AStarEval


class Search(ABC):
    evaluation_function: EvaluationFunction

    def __init__(self, problem: Problem):
        self.problem = problem

    def search(self, problem: Problem):
        pass


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

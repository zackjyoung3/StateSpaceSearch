from abc import ABC, abstractmethod
from problem import Problem
from evaluation_function import EvaluationFunction
from node import Node


class Search(ABC):
    @abstractmethod
    def search(self, problem: Problem, evaluation_function: EvaluationFunction):
        pass

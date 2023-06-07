from abc import ABC, abstractmethod
from problem import Problem
from typing import Callable
from node import Node


class Search(ABC):
    @abstractmethod
    def search(self, evaluation_function: Callable[[Node], float]):
        pass

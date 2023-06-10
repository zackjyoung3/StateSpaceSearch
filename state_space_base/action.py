from abc import ABC, abstractmethod
from state import State


class Action(ABC):
    cost: float

    @abstractmethod
    def take_action(self) -> State:
        """
        :return: the state that would result from taking this action
        """
        pass

    def get_cost(self) -> float:
        return self.cost

    @abstractmethod
    def __str__(self):
        pass


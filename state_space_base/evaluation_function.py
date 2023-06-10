from abc import ABC, abstractmethod
from state import State


class EvaluationFunction(ABC):
    @abstractmethod
    def evaluate(self, state: State, cost: float):
        pass


class CostFunction(EvaluationFunction):
    def evaluate(self, state: State, cost: float):
        return cost


class HeuristicEvaluationFunction(EvaluationFunction):
    def __init__(self, goal_state: State = None):
        self.goal_state = goal_state
    @abstractmethod
    def evaluate(self, state: State, cost: float):
        pass

    def set_goal_state(self, goal_state: State):
        self.goal_state = goal_state


class AStarEval(EvaluationFunction):
    def __init__(self, heuristic_eval_func: HeuristicEvaluationFunction):
        self.cost_func = CostFunction()
        self.heuristic_eval_func = heuristic_eval_func

    def evaluate(self, state: State, cost: float):
        return self.cost_func.evaluate(state, cost) + self.heuristic_eval_func.evaluate(state, cost)

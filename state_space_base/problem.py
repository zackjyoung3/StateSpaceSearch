from abc import ABC, abstractmethod
from state import State
from state_space_base.action import Action
from state_space_base.evaluation_function import HeuristicEvaluationFunction


class Problem(ABC):
    def __init__(self, initial_state: State, goal_state: State, heuristic_eval: HeuristicEvaluationFunction):
        self.initial_state = initial_state
        self.goal_state = goal_state
        assert issubclass(type(heuristic_eval), HeuristicEvaluationFunction)
        self.heuristic_eval = heuristic_eval
        heuristic_eval.set_goal_state(goal_state)

    def get_initial_state(self) -> State:
        return self.initial_state

    def is_goal_state(self, state: State) -> bool:
        """
        :param state: a state in the problem
        :return: determine if the state is the goal state for the problem
        """
        return state == self.goal_state

    @abstractmethod
    def get_actions(self, state: State) -> list[Action]:
        """
        :param state: a state in the problem
        :return: all actions that can be taken from this state
        """
        pass

    def get_result(self, state: State, action: Action) -> State:
        """
        :param state: a state in the problem
        :param action: the action to be taken from that state
        :return: the state that results from taking that action in the particular state
        """
        if action not in self.get_actions(state):
            raise ValueError(f"Action '{action}' not in actions from state.")
        return action.take_action()

    def get_action_cost(self, state: State, action: Action) -> float:
        """
        :param state: a state in the problem
        :param action: the action to be taken from that state
        :return: the cost of performing that action
        """
        if action not in self.get_actions(state):
            raise ValueError(f"Action '{action}' not in actions from state.")
        return action.get_cost()

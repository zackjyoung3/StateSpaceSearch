from evaluation_function import HeuristicEvaluationFunction
from city import City
from constant_cities_graph import euclidean_distance


class Euclidean_Distance(HeuristicEvaluationFunction):
    def __init__(self, goal_state: City = None):
        super().__init__()

    def evaluate(self, city: City, cost: float):
        if self.goal_state is None:
            raise RuntimeError("Did not set the goal state for the heuristic evaluation function")
        else:
            return euclidean_distance(city.x, city.y, self.goal_state.x, self.goal_state.y)

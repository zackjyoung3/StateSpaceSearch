from state_space_base.evaluation_function import HeuristicEvaluationFunction
from city_problem.city import City
from city_problem.constant_cities_graph import euclidean_distance as distance


class Euclidean_Distance(HeuristicEvaluationFunction):
    def __init__(self, goal_state: City = None):
        super().__init__(goal_state)

    def evaluate(self, city: City, cost: float):
        if self.goal_state is None:
            raise RuntimeError("Did not set the goal state for the heuristic evaluation function")
        else:
            return distance(city.x, city.y, self.goal_state.x, self.goal_state.y)


euclidean_distance = Euclidean_Distance()

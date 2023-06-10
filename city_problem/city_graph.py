from city_problem.city import City
from city_route import CityRoute
from euclidean_heuristic_eval import euclidean_distance
from state_space_base.problem import Problem


class CityGraph(Problem):
    def __init__(self, graph: dict, initial_city_string: str, goal_city_string: str):
        cities = {city[0]: City(city[0], city[1], city[2]) for city in graph}
        self.cities_actions = {
            cities[city[0]]: [CityRoute(cities[city[0]], cities[temp[0][0]], temp[1]) for temp in actions]
            for city, actions in graph.items()
        }

        super().__init__(cities[initial_city_string], cities[goal_city_string], euclidean_distance)

    def get_actions(self, state: City) -> list[CityRoute]:
        """
        :param state: a state in the problem
        :return: all actions that can be taken from this state
        """
        return self.cities_actions[state]

    def __str__(self):
        string = 'Initial State: {}\n'.format(self.initial_state)
        string += 'Goal State: {}\n'.format(self.goal_state)
        for state in self.cities_actions:
            string += str(state) + '\n'
            for action in self.cities_actions[state]:
                string += '\t{}\n'.format(str(action))
        return string


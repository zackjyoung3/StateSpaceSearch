from state_space_base.action import Action
from city_problem.city import City


class CityRoute(Action):
    def __init__(self, start_city: City, city_to_travel_to: City, minutes: float):
        self.start_city = start_city
        self.city_to_travel_to = city_to_travel_to
        self.cost = minutes

    def take_action(self) -> City:
        """
        :return: the state that would result from taking this action
        """
        return self.city_to_travel_to

    def get_cost(self) -> float:
        return self.cost

    def __str__(self):
        return f"{self.start_city} ----{self.cost} min----> {self.city_to_travel_to}"

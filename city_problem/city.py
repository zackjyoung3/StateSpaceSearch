from state_space_base.state import State


class City(State):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __hash__(self):
        # may be duplicate city names across states => use the full string rep
        return hash(self.__str__())

    def __eq__(self, other):
        return self.name == other.name and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"City: name: {self.name} x: {self.x} y: {self.y}"

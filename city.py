from state import State


class City(State):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
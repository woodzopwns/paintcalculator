import math


class House:
    def __init__(self):
        self._rooms = set()

    def add_room(self, new_room):
        self._rooms.add(new_room)

    def get_house_area(self):
        area = 0
        for room in self._rooms:
            area += room.get_total_area()
        return area


class Room:
    def __init__(self):
        self._walls = set()

    def add_wall(self, new_wall):
        self._walls.add(new_wall)

    def get_total_area(self):
        total_area = 0
        for wall_iteration in self._walls:
            total_area += wall_iteration.get_area()

        return total_area


class Wall:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._area = self._width * self._height

    def get_area(self):
        return self._area

    def recalculate_area(self, obstruction):
        self._area -= obstruction

    def add_circular_obstruction(self, radius):
        self.recalculate_area(radius ** 2 * math.pi)

    def add_square_obstruction(self, height, width):
        self.recalculate_area(height * width)


class Paint:
    def __init__(self, price, paintable_area):
        self._price_per_metre = price / paintable_area

    def calculate_price(self, area):
        return self._price_per_metre * area
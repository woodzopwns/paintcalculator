import math


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
        self._price = price
        self._paintable_area = paintable_area

    def calculate_price(self, area):
        return self._price / self._paintable_area * area


wall = Wall(10, 10)
blue_paint = Paint(10, 10)
wall.add_square_obstruction(1, 1)
price = blue_paint.calculate_price(wall.get_area())

print(price)

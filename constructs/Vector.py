import math
from typing import Union


class Vector2D:
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x_value = float(x)
        self.y_value = float(y)

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, *self)

    def __iter__(self):
        yield self.x_value
        yield self.y_value

    def __add__(self, other):
        return Vector2D(*[value_1 + value_2 for value_1, value_2 in zip(self, other)])

    def __iadd__(self, other):
        self.x_value += other.x_value
        self.y_value += other.y_value

        return self

    def __sub__(self, other):
        return Vector2D(self.x_value - other.x_value, self.y_value - other.y_value)

    def __isub__(self, other):
        self.x_value -= other.x_value
        self.y_value -= other.y_value

        return self

    def __mul__(self, other):
        return Vector2D(*[value_1 * other for value_1 in self])

    def __rmul__(self, other):
        return Vector2D(*[other * value_1 for value_1 in self])

    def __imul__(self, other):
        self.x_value *= other
        self.y_value *= other

        return self

    def __truediv__(self, other):
        return Vector2D(*[value_1 / other for value_1 in self])

    def __pow__(self, power, modulo=None):
        x_value = self.x_value**power
        y_value = self.y_value**power

        return Vector2D(x_value, y_value)

    def __abs__(self):
        return math.hypot(*self)

    def __getitem__(self, item):
        if item == 0:
            return self.x_value
        elif item == 1:
            return self.y_value
        else:
            raise IndexError(f"Index {item} is out of range.")

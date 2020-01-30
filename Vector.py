
class Vector:
    def __init__(self, values: list):
        self.x_value = values[0]
        self.y_value = values[1]

    def __repr__(self):
        return f"| {self.x_value} |\n| {self.y_value} |"

    def __add__(self, other):
        x_value = self.x_value + other.x_value
        y_value = self.y_value + other.y_value

        return Vector([x_value, y_value])

    def __iadd__(self, other):
        x_value = self.x_value + other.x_value
        y_value = self.y_value + other.y_value

        return Vector([x_value, y_value])

    def __sub__(self, other):
        x_value = self.x_value - other.x_value
        y_value = self.y_value - other.y_value

        return Vector([x_value, y_value])

    def __isub__(self, other):
        x_value = self.x_value - other.x_value
        y_value = self.y_value - other.y_value

        return Vector([x_value, y_value])

    def __mul__(self, other):

        x_value = self.x_value * other
        y_value = self.y_value * other

        return Vector([x_value, y_value])

    def __rmul__(self, other):

        x_value = self.x_value * other
        y_value = self.y_value * other

        return Vector([x_value, y_value])

    def __imul__(self, other):

        x_value = self.x_value * other
        y_value = self.y_value * other

        return Vector([x_value, y_value])

    def __truediv__(self, other):
        x_value = self.x_value / other
        y_value = self.y_value / other

        return Vector([x_value, y_value])

    def __pow__(self, power, modulo=None):
        x_value = self.x_value**power
        y_value = self.y_value**power

        return Vector([x_value, y_value])

    def __abs__(self):
        x_value = abs(self.x_value)
        y_value = abs(self.y_value)

        return Vector([x_value, y_value])

    def __getitem__(self, item):
        if item == 0:
            return self.x_value
        elif item == 1:
            return self.y_value
        else:
            raise IndexError(f"Index {item} is out of range.")

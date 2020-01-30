from Vector import Vector


class Object:
    def __init__(self, mass: float, position: list, velocity: list, name: str):
        self.name = name
        self.mass = mass
        self.x_positions = [position[0]]
        self.y_positions = [position[1]]
        self.position = Vector(position)
        self.velocity = Vector(velocity)

    def update_velocity(self, other_mass: float, other_position: Vector, time_increment: float):
        gravitational_const = -6.674 * 10 ** -11
        exponent = gravitational_const * other_mass * self.mass

        magnitude_distance = ((self.position[0] - other_position[0]) ** 2 +
                              (self.position[1] - other_position[1]) ** 2) ** 0.5

        force_gravity = exponent / magnitude_distance ** 2

        force_gravity = force_gravity * (self.position / (self.position[0] ** 2 + self.position[1] ** 2) ** 0.5)

        exponent = time_increment / self.mass
        delta_velocity = force_gravity * exponent

        self.velocity += delta_velocity

    def update_position(self, time_increment: float):
        self.position += self.velocity * time_increment

    def update_attributes(self):
        self.x_positions.append(self.position[0])
        self.y_positions.append(self.position[1])

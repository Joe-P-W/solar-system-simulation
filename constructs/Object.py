import json

from constructs.Vector import Vector2D
from constructs.constants import GRAVITATIONAL_CONSTANT


class Object:
    def __init__(self, mass: float, position: list, velocity: list, name: str):
        self.name = name
        self.mass = mass
        self.x_positions = [position[0]]
        self.y_positions = [position[1]]
        self.position = Vector2D(*position)
        self.velocity = Vector2D(*velocity)

    @classmethod
    def from_json(cls, path: str):
        with open(path, "r") as input_file:
            attributes = json.load(input_file)

        return cls(**attributes)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def update_velocity(self, other_mass: float, other_position: Vector2D, time_increment: float):

        force_gravity = GRAVITATIONAL_CONSTANT * other_mass * self.mass / abs(self.position - other_position) ** 2

        self.velocity += force_gravity * (self.position / abs(self.position)) * (time_increment / self.mass)

    def update_position(self, time_increment: float):
        self.position += self.velocity * time_increment

    def update_attributes(self):
        self.x_positions.append(self.position[0])
        self.y_positions.append(self.position[1])

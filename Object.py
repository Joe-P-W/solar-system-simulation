
class Object:
    def __init__(self, mass: float, position: list, velocity: list):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.x_positions = [position[0]]
        self.y_positions = [position[1]]

    def update_velocity(self, other_mass: float, other_position: list, time_increment: float):
        gravitational_const = -6.674 * 10**-11

        self.velocity[0] += (((gravitational_const * other_mass * time_increment) /
                              (self.position[0] - other_position[0])**2))
        self.velocity[1] += (((gravitational_const * other_mass * time_increment) /
                              (self.position[1] - other_position[1])**2))

    def update_position(self, time_increment: float):

        self.position[0] += self.velocity[0] * time_increment
        self.position[1] += self.velocity[1] * time_increment

    def update_attributes(self):

        self.x_positions.append(self.position[0])
        self.y_positions.append(self.position[1])

from typing import List

from constructs.Object import Object
from matplotlib import pyplot as plt
import time


def calculate_solar_system(_objects: List[Object], _time_increment: int, _simulation_length: int):
    for i in range(int((_simulation_length / _time_increment))):
        for index, _object in enumerate(_objects):
            other_objects = _objects[:index] + _objects[index + 1:]
            for other_object in other_objects:
                _object.update_velocity(other_object.mass, other_object.position, _time_increment)

        for _object in _objects:
            _object.update_position(_time_increment)
            _object.update_attributes()


if __name__ == "__main__":

    objects = ["sun", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
    objects = [Object.from_json(f"object_attributes/{_object}.json") for _object in objects]

    time_increment = 1000
    simulation_length = 3.154 * 10 ** 7

    t1 = time.time()
    calculate_solar_system(objects, time_increment, simulation_length)
    print(f"{time.time() - t1}")

    ax = plt.figure(figsize=(12, 12))
    plt.xlabel("x distance from the Sun (metres)")
    plt.ylabel("y distance from the Sun (metres)")
    for _object in objects:
        plt.plot(_object.x_positions, _object.y_positions, label=_object.name)

    boundary = 6 * 10 ** 12
    plt.xlim(-boundary, boundary)
    plt.ylim(-boundary, boundary)
    plt.legend()

    plt.show()

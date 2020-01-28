import time

from Object import Object
from threading import Thread
import matplotlib.pyplot as plt
import os


def run_calculation(_object: Object, _index: int, _time_increment: int):
    global objects

    other_objects = objects[:_index] + objects[_index + 1:]
    for other_object in other_objects:
        _object.update_velocity(other_object.mass, other_object.position, _time_increment)


def update_attributes(_object: Object, _time_increment: int):
    _object.update_position(_time_increment)
    _object.update_attributes()


if __name__ == "__main__":
    t1 = time.time()

    neptune = Object(1.024*10**26, [4.495*10**12, 0], [0, 5.43*10**3], "Neptune")
    uranus = Object(8.681*10**25, [2.871*10**12, 0], [0, 6.8*10**3], "Uranus")
    saturn = Object(5.683*10**26, [1.434*10**12, 0], [0, 9.68*10**3], "Saturn")
    jupiter = Object(1.898*10**27, [778.5**9, 0], [0, 13.07*10**3], "Jupiter")
    mars = Object(6.39*10**23, [234.28*10**9, 0], [0, 24*10**3], "Mars")
    earth = Object(5.972*10**24, [147.31*10**9, 0], [0, 29.75*10**3], "Earth")
    venus = Object(4.867*10**24, [108.11*10**9, 0], [0, 35*10**3], "Venus")
    mercury = Object(3.285*10**23, [53.761*10**9, 0], [0, 48*10**3], "Mercury")
    sun = Object(1.989*10**30, [1, 1], [0, 0], "Sun")

    time_increment = 100
    objects = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    if os.cpu_count() < len(objects):
        raise Exception(f"CPU core count too low a minimum of {len(objects)} is need and found {os.cpu_count()}")

    for i in range(int(((3.154*10**7)/time_increment))):

        threads = []
        for index, _object in enumerate(objects):
            threads.append(Thread(target=run_calculation, args=(_object, index, time_increment)))

        for thread in threads:
            thread.start()
            thread.join()

        threads = []
        for _object in objects:
            threads.append(Thread(target=update_attributes, args=(_object, time_increment)))

        for thread in threads:
            thread.start()
            thread.join()

    ax = plt.figure(figsize=(12, 12))
    plt.xlim(-4.5*10**12, 4.5*10**12)
    plt.ylim(-4.5*10**12, 4.5*10**12)
    plt.xlabel("x distance from the Sun (metres)")
    plt.ylabel("y distance from the Sun (metres)")
    for _object in objects:
        plt.plot(_object.x_positions, _object.y_positions, label=_object.name)

    plt.legend()
    plt.show()
    print(f"Multithread took: {time.time() - t1}")
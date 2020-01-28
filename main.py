from Object import Object
import matplotlib.pyplot as plt

reduction = 12

earth = Object(5.972*10**24, [147.31*10**9, 0], [0, 29.75*10**3])
mercury = Object(3.285*10**23, [53.761*10**9, 0], [0, 48*10**3])
sun = Object(1.989*10**30, [1, 1], [0, 0])

time_increment = 100
objects = [sun, earth]

for i in range(int(((3.154*10**7)/time_increment))):
    for index, _object in enumerate(objects):
        other_objects = objects[:index] + objects[index+1:]
        for other_object in other_objects:
            try:
                _object.update_velocity(other_object.mass, other_object.position, time_increment)
                _object.update_position(time_increment)
                _object.update_attributes()
            except OverflowError:
                pass


ax = plt.figure(figsize=(12, 12))
plt.xlim(-200000000000, 200000000000)
plt.ylim(-200000000000, 200000000000)
for _object in objects:
    plt.plot(_object.x_positions, _object.y_positions)

plt.show()
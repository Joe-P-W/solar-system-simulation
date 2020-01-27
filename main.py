from Object import Object
import matplotlib.pyplot as plt

earth = Object(5.972*10**24, [147.31*10**9, 0], [-460, 460])
sun = Object(1.989*10**30, [0, 0], [0, 0])

time_increment = 100.0
objects = [sun, earth]

for i in range(int((3.154*10**7)/time_increment)):
    for index, _object in enumerate(objects):
        for other_object in objects[:index] + objects[index+1:]:
            _object.update_velocity(other_object.mass, other_object.position, time_increment)
            _object.update_position(time_increment)

    for _object in objects:
        _object.update_attributes()

ax = plt.figure(figsize=(12, 12))
plt.xlim(-200000000000, 200000000000)
plt.ylim(-200000000000, 200000000000)
for _object in objects:
    plt.plot(_object.x_positions, _object.y_positions)

print(earth.x_positions)
plt.show()
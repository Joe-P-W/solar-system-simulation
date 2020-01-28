from Object import Object
import matplotlib.pyplot as plt

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

for i in range(int(((3.154*10**7)/time_increment))):
    for index, _object in enumerate(objects):
        other_objects = objects[:index] + objects[index+1:]
        for other_object in other_objects:
            _object.update_velocity(other_object.mass, other_object.position, time_increment)

    for _object in objects:
        _object.update_position(time_increment)
        _object.update_attributes()

ax = plt.figure(figsize=(12, 12))
plt.xlim(-4.5*10**12, 4.5*10**12)
plt.ylim(-4.5*10**12, 4.5*10**12)
plt.xlabel("x distance from the Sun (metres)")
plt.ylabel("y distance from the Sun (metres)")
for _object in objects:
    plt.plot(_object.x_positions, _object.y_positions, label=_object.name)

plt.legend()
plt.show()
from itertools import product

print("x y z")
for x, y, z in product(range(2), repeat=3):
    if ((x == z) or (x <= (y and z))) == 0:
        print(x, y, z)

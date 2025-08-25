from itertools import product

print("x y z w")
for x, y, z, w in product(range(2), repeat=4):
    if (w == (not(z == y))) and (z == (y <= x)):
        print(x, y, z, w)
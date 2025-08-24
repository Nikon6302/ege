from itertools import product

print("w z y x")

for w, z, y, x in product(range(2), repeat=4):
    if (w == (not(z == y))) and (z == (y <= x)):
        print(w, z, y, x)
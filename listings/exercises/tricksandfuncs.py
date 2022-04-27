"""
Script for random useful functions and tricks
"""

# map - map a function to iterate on all elements
minutes = map(lambda t: t[len(t) - 2 :], ["1200", "1213", "1247", "1306"])
print(list(minutes))

planeQuantities = [0, 1, 4]
planeTypes = ["jabiru", "cirrus", "diamond"]
planes = map(lambda x, y: str(x) + " " + y + "s", planeQuantities, planeTypes)
print(list(planes))

# sorting based on a key function
keySorting = sorted([0, 1, 4], key=lambda x: 0 if x == 4 else x)
print("key sorting ", keySorting)

# more useful stuff for iterables
randoString = " pilot "
newRandoString = randoString.join(["commercial", "license"])
print(newRandoString)

clean = randoString.strip()  # removes leading and trailing whitespace in a string
print(clean)

filtered = filter(
    lambda planes: True if planes < 4 else False, planeQuantities
)  # removes false values
print(list(filtered))

zipped = list(
    zip(planeQuantities, planeTypes)
)  # combines two sequences like a zipper - (0,0), (1,1) etc
print(zipped)

unzipped = list(zip(*zipped))  # unpacks, rezips
print(unzipped)

enum = enumerate(planeTypes)
print(list(enum))

# swapping variables - python magic
a, b = "helicopter", "aeroplane"
print(a, b)
a, b = b, a
print(a, b)


# sweet argument unpacks for functions
def func(x, y, z):
    return x + y * z


print(func(*planeQuantities))
dict = {
    "y": 0,
    "x": 1,
    "z": 4,
}  # note strings need to be the argument variables, but not in order
print(func(**dict))

# merge dictionaries
dictA = {"cat": 2, "dog": 3}
dictB = {"bird": 3, "horse": 1}
dictC = {**dictB, **dictA}
print(dictC)

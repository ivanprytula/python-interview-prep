"""
Script for playing with basic python data structures
"""

# lists - square brackets - mutable (changeable)
listA = [1, 2, 3]
print("listA ", listA)

# list methods
listA.append(4)
print("listA appended ", listA)

listA.remove(2)
print("listA remove ", listA)

listA.reverse()
print("listA reverse ", listA)

print("listA length", len(listA))

listA.sort()  # sorts in ascending order
print("listA sort ", listA)

a = listA.index(4)  # returns first index of value
print(a)

listA.append(4)
print(
    "index of 4 = ", listA.index(4, 0, 3)
)  # returns the index of the first value 4, between indices 0 and 3

listA.pop()
print("listA pop ", listA)

# sets - braces/curly brackets - unordered structure of unique elements
setA = {10, 20, 30, 40, 50}
print(setA)

# set methods
setA.add(100)
print("setA add ", setA)

setB = {10, 20, 40, 50, 100}
print("setB and setA difference ", setA.difference(setB))

print("setB max ", max(setB))

print("setA and setB intersection ", setB.intersection(setA))

setB.discard(100)
print("setB discarded 100 ", setB)

# tuples - parantheses or round brackets - immutable (cannot be changed)
tupleA = ("plane", "car", "train", "ship", "car", "car")

print("train index = ", tupleA.index("train"))

print("car count = ", tupleA.count("car"))

# dictionary - braces/curly brackets - key:value pairs, super useful!
hojDict = {"tees": 10, "shoes": 12, "jeans": 8}
print(hojDict)

# dictionary methods
print(hojDict["tees"], hojDict["jeans"])
print(hojDict["jeans"] < hojDict["tees"])

hojDict["shoes"] = 15
print(hojDict)

hojDict["t-shirts"] = hojDict.pop(
    "tees"
)  # using dict.pop to replace a key - pop returns the value of the popped key:value pair
print(hojDict)

print(hojDict.keys(), hojDict.values())
popped = hojDict.popitem()

print("popped jeans ", hojDict, popped)  # note that popped is returned as a tuple

for (
    i,
    j,
) in (
    hojDict.items()
):  # can use items function to return values - useful in loops. Note use of membership
    # keyword 'in'
    print(i) if j > 10 else None
print("jeans" in hojDict)
print("t-shirts" in hojDict)

# basic data structures comprehensions
listB = [
    ("brown " + x) for x in ["cat", "dog", "mouse", "horse"]
]  # note this is a list, since square brackets... which means?? It's mutable
print(listB)

setC = {
    x * y for x in range(6) for y in range(2) if x > y
}  # cray what you can get into one line in Python! This is a set - also works for list
print(setC)

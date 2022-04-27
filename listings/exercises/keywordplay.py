"""
Script for keyword and function play
"""

# bool algebra
x, y = True, False
print(x and y)  # false
print(x or y)  # true
print(not x)  # false

# aviation for loop
hangar = ["cessna", "cherokee", "R44", "squirrel", "longranger"]
for aircraft in hangar:
    print(aircraft)

# the 'aviaiton is going out of business' while loop, with if statement for a conditional break or continue
while len(hangar) > 0:
    if hangar == ["cessna"]:
        break
    hangar = hangar[: len(hangar) - 1]
    print(hangar)
print("While loop with break complete! You get to keep your Cessna")

newHangar = ["aerostar", "R22", "EC130", "cheiftain", "H300"]
print(newHangar)
while len(newHangar) > 0:
    newHangar = newHangar[: len(newHangar) - 1]
    if len(newHangar) == 2:
        continue
    print(newHangar)
print(
    "While loop with continue complete! You lost your R22 and EC130 in the same hit... dayuuuuum"
)

# conditionals
x = int(input("How many planes do you have? "))
if x > 3:
    print("You must work for ANZ")
elif 1 <= x < 3:
    print("Congratulations, you have money and a rad hobby")
else:
    print("You should really buy a plane")

# in - super easy way to check element in sequence
hojTuple = (23, 45, 97, 104)
print(45 in hojTuple, 67 in hojTuple)

# is - checks if two elements point to the same object
a = b = 6
print(a is b)  # true
print([3] is [3])  # false - two separate objects defined, happen to contain same value

# lambda - the magical anonymous function, most useful as an argument in a higher order function
c = (lambda d: d + 3)(3)
print(c)  # OR....

altC = lambda d: d + 3  # you can name the function and call it
print(altC(5))

higherOrderC = lambda d, func: d + func(d)  # higher order example
print(higherOrderC(2, lambda d: d * d))


# using return in a function
def beerFunction(day):
    beers = 0
    if day == "Friday":
        beers = 3
    elif day == "Wednesday" or "Thursday":
        beers = 1
    return beers


print("Tonight you can have: ", beerFunction("Friday"), " beers")

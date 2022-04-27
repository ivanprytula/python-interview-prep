"""
Script for playing with basic python data types
"""

# bool
x, y = True, False
print(x == y, x != y)
a, b = 2, 3
print(a < b, b < a)

# integer
x = 3
y = 6
z = y / x
print("first z type", type(z))  # float

z = y // x
print("second z type", type(z))  # integer
a = 3
b = 2
print(a / b)
print(a // b)  # discards fractional part to return int
print(a % b)  # returns remainder of the division
print(a * b)  # multiplication
print(a ** 2)  # power

# casting
c = 2.9
print(c, type(c))
c = int(c)
print(c, type(c))
c = float(c)
print(c, type(c))  # note value of new float
c = str(c)
print(c, type(c))  # note string not printed!
d = int(5)
e = str(d)
print(d, type(d))

# strings
s = "python is the best ever"
print(type(s))
t = "and this is also a string"
r = """\nthis
is a
string across
multiple lines"""
print(s, t, r)
i = str(666)  # cast the devil as a string
print(i, type(i))
print("concat" + "enation")  # run strings together
print(
    "newline\nspace tab\t"
)  # whitespace special characters for strings - avoid with r at beginning of string

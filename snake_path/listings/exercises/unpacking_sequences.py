items = (1, 2)
print(items)

# NB: Unpacking
a, b = (1, 2)
# c, _ = (1, 2)  # we just don't need second variable
# d, e, f = (4, 5)
# g, h, i = (6, 7, 8, 9)
g, h, *i = (6, 7, 8, 9)  # we can unpack rest of the tuple in variable with asterisk
j, k, *_ = (10, 11, 12, 13)
l, m, *n, o = (14, 15, 16, 17)
p, q, *_, s = (18, 19, 20, 21)
# t, u, *_, v, *w = (22, 23, 24, 25, 26, 27, 28, 29)  # SyntaxError: two starred expressions in assignment

print(a)
# print(b)
print(g, h, i)

print(j, k)

print(l, m, n, o)
# print(t, u, v, w)

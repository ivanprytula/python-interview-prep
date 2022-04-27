import sys

print(1, 2, 3, 4, 5)  # 1 2 3 4 5
print((1, 2, 3, 4, 5))  # (1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep=", ")  # 1, 2, 3, 4, 5
print(1, 2, 3, 4, 5, sep=" | ")  # 1 | 2 | 3 | 4 | 5
print(1, 2, 3, 4, 5, sep=" | ", end="\n\n")
print(1, 2, 3, 4, 5, end="")

print('You messed up!', file=sys.stderr)

with open("example.txt", "w") as f:
    # f.write('testtext')
    print("Here is some file content", file=f)

# bad: but still possible
for _ in range(10):
    print(_)

# good:
for _ in range(10):
    print("Hello!")

import sys

# Convert String list to ascii values

# Method 1.: using loop + ord()
test_str = "let's do more Python!"
res1 = ''
for elem in test_str:
    res1 += "".join(str(ord(elem)))
print(res1)
print('size of res1', sys.getsizeof(res1))

# Method 2: list comprehension
test_str2 = "let's do more Python!"
res2 = ''.join([str(ord(elem)) for elem in test_str2])
print(res2)
print('size of res2', sys.getsizeof(res2))

print(res1 == res2)

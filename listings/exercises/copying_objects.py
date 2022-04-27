import copy

# shallow copy
# base  types
number = 123
copied_num = copy.copy(number)
print(id(number))
print(id(copied_num))

number += 10
print(id(copied_num))

# compound types
lst_one = [[1, 2, ], ['a', 'b']]
copied_lst_one = copy.copy(lst_one)
print(id(lst_one))
print(id(copied_lst_one))
print(copied_lst_one)

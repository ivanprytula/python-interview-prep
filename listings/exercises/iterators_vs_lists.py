import cProfile
import random
import sys

l_in = [random.random() for _ in range(100000)]
my_iter_list = iter(l_in)
my_gen_comprehension = (random.random() for _ in range(100000))

print(F'type = {type(l_in)}; \t id = {id(l_in)};  \t sys.getsizeof(l_in) == {sys.getsizeof(l_in)} bytes')
print(
    F'type = {type(my_iter_list)}; \t id = {id(my_iter_list)};  \t sys.getsizeof(my_iter_list) == '
    F'{sys.getsizeof(my_iter_list)} bytes')
print(
    F'type = {type(my_gen_comprehension)}; \t id = {id(my_gen_comprehension)};  \t sys.getsizeof(l_in) == '
    F'{sys.getsizeof(my_gen_comprehension)} bytes')


def check_list(l_input):
    l1 = sorted(l_input)
    l2 = [i * 2 for i in l1]
    return l2


def check_iterator(l_input):
    l1 = sorted(l_input)
    l2 = [i * 2 for i in l1]
    return l2


def check_generator(l_input):
    l1 = sorted(l_input)
    l2 = [i * 2 for i in l1]
    return l2


cProfile.run('check_list(l_in)')
cProfile.run('check_iterator(l_in)')
cProfile.run('check_generator(l_in)')

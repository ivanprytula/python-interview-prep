import logging
import os


# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.warning('And this, too')
# logging.info('So should this')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


class DemoClassName:
    # Initializer Overloading
    def __init__(self, a=None):
        self.a = a

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.a!r})'

    def __str__(self):
        return str(self.a)

    @classmethod
    def get_class_name(cls):
        return cls.__name__


demo_obj = DemoClassName(a=10)


# print(DemoClassName.get_class_name())  # DemoClassName
# print(demo_obj)  # 10
# print(demo_obj.__repr__())  # DemoClassName(10)


# NB: Custom context manager
class ManagedWriteFile:
    """
    - Enter() should lock the resources and optionally return an object.
    - Exit() should release the resources.
    - Any exception that happens inside the with block is passed to the exit() method.
    - If it wishes to suppress the exception it must return a true value.
    """

    def __init__(self, file_name, mode='r'):
        self.mode = mode
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exception_type, exception, exception_tb):
        if self.file:
            self.file.close()


# with ManagedWriteFile('hello.md', 'w') as f:
#     f.write('requests==2.26.0')
#     f.write('\n')
#     f.write('Django>=3.2.7')

class A:
    pass


class B:
    pass


# Multiple Inheritance
class C(A, B):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        return str(self.age)


# Hybrid Inheritance
class Employee(Person, C):
    """Mechanism that restricts objects to attributes listed in 'slots' and significantly reduces their memory
    footprint."""

    # Class variable shared by all instances, instance variable unique to each instance.

    __slots__ = ('staff_num', '__a', 'extra')

    def __init__(self, name, age, staff_num, __a: str):
        super().__init__(name, age)
        self._extra = "extra eggs"  # Protected variable
        self.staff_num = staff_num
        self.__a = __a  # semi-Private variable

    # Polymorphism
    def show_age(self):
        return self.age + 10

    # Pythonic way of implementing getters and setters.
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @a.deleter
    def a(self):
        del self.__a
        print('oh, no!!')


employee_one = Employee('John', 33, 100, 'foo')


# print('employee_one.a:', employee_one.a)
# print(employee_one.__a)  # AttributeError: 'Employee' object has no attribute '__a'
# print(employee_one.a)  # foo
# del employee_one.a  # oh, no!!

# print(Employee.mro())
# [<class '__main__.Employee'>, <class '__main__.Person'>, <class '__main__.C'>, <class '__main__.A'>,
# <class '__main__.B'>, <class 'object'>]

class Counter:
    """
    - Any object that has methods next() and iter() is an iterator.
    - Next() should return next item or raise StopIteration.
    - Iter() should return 'self'.

    Python has many iterator objects:

    Sequence iterators returned by the iter() function, such as list_iterator and set_iterator.
    Objects returned by the itertools module, such as count, repeat and cycle.
    Generators returned by the generator functions and generator expressions.
    File objects returned by the open() function, etc.
    """

    def __init__(self):
        self.i = 0

    def __next__(self):
        self.i += 1
        return self.i

    def __iter__(self):
        return self


# counter = Counter()


# print(next(counter), next(counter))  # 1 2


class CallableCounter:
    """
    All functions and classes have a call() method, hence are callable.
    """

    def __init__(self):
        self.i = 0

    def __call__(self):
        self.i += 1
        return self.i


# call_counter = CallableCounter()
# print(call_counter(), call_counter(), call_counter())

# Metaprogramming
# <class> = type('<class_name>', <parents_tuple>, <attributes_dict>)
Z = type('Z', (), {'a': 'abcde', 'b': 12345})
z = Z()
print(z)  # <__main__.Z object at 0x7f58a56bfb20>


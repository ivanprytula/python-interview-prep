class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet_user(self):
        print(f'Hello, {self.age}')


print(Parent.mro())
print(Parent.__mro__)


class Child(Parent):
    """Derived class."""

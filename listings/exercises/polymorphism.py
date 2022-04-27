class Parent():
    def __init__(self):
        print('Parent init')

    def method(self):
        print('Parent method')


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def method(self):
        super().method()


child = Child()  # Parent init
child.method()  # Parent method

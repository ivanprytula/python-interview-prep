"""
Demonstration of monkey patching.
"""


class A:
    """Simple demo class."""

    def __init__(self, name=''):
        self.name = name

    @staticmethod
    def func():
        """Simple demo function with print statement."""
        print("func() is being called")


DEMO_VAR = 'don"t change me!'

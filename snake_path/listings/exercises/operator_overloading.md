```python
class Point:
    def __init__(self, x=0, y=0, cart=None):
        self.x = x
        self.y = y
        self.cart = list(cart)

    def __str__(self):
        return f'({self.x}, {self.y})'

    # adding overloading
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # 'less than' overloading
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

    # Giving a Length to Your Objects Using len()
    def __len__(self):
        return len(self.cart)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 + p2)
```

| Operator             | Expression   | Internally              |
|----------------------|--------------|-------------------------|
|Addition              | `p1 + p2`    | `p1.__add__(p2)`        |
|Subtraction           | `p1 - p2`    | `p1.__sub__(p2)`        |
|Multiplication        | `p1 * p2`    | `p1.__mul__(p2)`        |
|Power                 | `p1 ** p2`   | `p1.__pow__(p2)`        |
|Division              | `p1 / p2`    | `p1.__truediv__(p2)`    |
|Floor Division        | `p1 // p2`   | `p1.__floordiv__(p2)`   |
|Remainder (modulo)    | `p1 % p2`    | `p1.__mod__(p2)`        |
|Bitwise Left Shift    | `p1 << p2`   | `p1.__lshift__(p2)`     |
|Bitwise Right Shift   | `p1 >> p2`   | `p1.__rshift__(p2)`     |
|Bitwise AND           | `p1 & p2`    | `p1.__and__(p2)`        |
|Bitwise OR            | p1 &#124; p2 | `p1.__or__(p2)`         |
|Bitwise XOR           | `p1 ^ p2`    | `p1.__xor__(p2)`        |
|Bitwise NOT           | `~p1`        | `p1.__invert__(p2)`     |
|----------------------|--------------|-------------------------|
|Less than             | `p1 < p2`    | `p1.__lt__(p2)`        |
|Less than or equal to | `p1 <= p2`    | `p1.__le__(p2)`        |
|Equal to              | `p1 == p2`    | `p1.__eq__(p2)`        |
|Not equal to          | `p1 != p2`    | `p1.__ne__(p2)`        |
|Greater than          | `p1 > p2`    | `p1.__gt__(p2)`        |
|Greater than/equal to | `p1 >= p2`    | `p1.__ge__(p2)`        |
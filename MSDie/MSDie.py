import random


class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides
    """

    def __init__(self, num_sides) -> None:
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self) -> int:
        self.current_value = random.randrange(self.num_sides) + 1
        return self.current_value

    def __str__(self) -> str:
        return str(self.current_value)

    def __repr__(self) -> str:
        return f"MSDie({self.num_sides}) : {self.current_value}"

    def __eq__(self, d2) -> bool:
        return self.current_value == d2.current_value

    def __lt__(self, d2) -> bool:
        return self.current_value < d2.current_value

    def __le__(self, d2) -> bool:
        return self.current_value <= d2.current_value

x = MSDie(6)
y = MSDie(7)

x.current_value = 6
y.current_value = 5

print(x == y)
print(x < y)
print(x > y)
print(x != y)
print(x<=y)
print(x>=y)
print(x is y)
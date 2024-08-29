class Rectangle:
    def __init__(self, lent, br) -> None:
        self.lent = lent
        self.br = br

    def __str__(self) -> str:
        return f"l = {self.lent}, b = {self.br}"

    def area(self):
        return self.lent * self.br

    def perimeter(self):
        return 2 * (self.lent + self.br)

    def is_sq(self):
        return self.lent == self.br


a = Rectangle(5, 6)
b = Rectangle(9, 10)
print(a)
print(b)

class Rectangle:
    def __init__(self, lent, br) -> None:
        self.lent = lent
        self.br = br

    def area(self):
        return self.lent * self.br

    def perimeter(self):
        return 2 * (self.lent + self.br)

    def is_sq(self):
        return self.lent == self.br
        # if self.lent == self.br:
        #     return True
        # return False


a = Rectangle(5, 6)
ar = a.area()
pr = a.perimeter()
sq = a.is_sq()
print(f"area of rect is : {ar}")
print(f"area of peri is : {pr}")
print(f"square : {sq}")

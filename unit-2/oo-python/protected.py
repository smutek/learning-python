# example of protected methods and attributes
class Protected:
    __name = "Security"

    def __method(self):
        return self.__name


# example with properties and setters
class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2


# quiz 1
class Rectangle:
    def __init__(self, w, l):
        self.w = w
        self.l = l

    @property
    def area(self):
        return self.l * self.w

    @property
    def perimeter(self):
        return (self.l * 2) + (self.w * 2)


# quiz 2
class Product:
    _price = 0.0
    tax_rate = 0.12

    def __init__(self, base_price):
        self._price = base_price

    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    @price.setter
    def price(self, price):
        self._price = price


rec = Rectangle(10, 15)
print(rec.area)
print(rec.perimeter)

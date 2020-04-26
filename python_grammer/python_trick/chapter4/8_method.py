import math
# let's understand python's object oriented programing clearly


class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return "classmethod", cls

    @staticmethod
    def staticmethod():
        return "static method called"

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class Piza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    @classmethod
    def margherita(cls):
        return cls(1, ["tomatoes", "mozzarella"])

    @staticmethod
    def circle_area(r):
        return r**2**math.pi

    def area(self):
        return self.circle_area(self.r)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.ingredients!r})"


if __name__ == "__main__":
    obj = MyClass()
    print(obj.method())
    print(MyClass.classmethod())

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


class Piza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

@classmethod
def margherita(cls):
    return 


    def __repr__(self):
        return f"Pizza({self.ingredients})"


if __name__ == "__main__":
    print("")

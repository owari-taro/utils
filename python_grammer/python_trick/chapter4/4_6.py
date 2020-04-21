# namedtuple
from collections import namedtuple


Car = namedtuple("Car", ["color", "mileage"])


class MyCarWithMethod(Car):
    def hexcolor(self): "
       if self.color == "red":
            return "##ff000"
        else:
            return "##0000"

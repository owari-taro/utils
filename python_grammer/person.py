class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.__height = height
        self.__weight = weight

    @property
    # with property, you can use this method without  parenthesis
    def weight(self):
        print("getter")
        return self.__weight

    @property
    def property_test(self):
        print("getter")
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        print("setter")
        if weight < 0:
            raise ValueError
        self.__weight = weight


    def __bool__(self):
        return bool(self.__weight)
    
  

if __name__ == "__main__":
    person = Person("hoge", 123, 70)
    print(person.weight)
    print(person.property_test)
    person.weight = 120
    print(person.weight)

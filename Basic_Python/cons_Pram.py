class Person:
    #D=Double  Under=Underscore
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name, self.age)


obj = Person("Noyon",27)
obj.printName()

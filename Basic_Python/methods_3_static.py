class Student1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def printInfo():
        print("I am from static method")

Student1.printInfo()
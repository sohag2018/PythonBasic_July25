import variable_1
variable_1.printInfo()

class Student:
    pass

class Student2(Student):
    school="Enthrall" #static variable
    #double underscore   dunder method
    #__init__ calls __new__ method to create obj of the class
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
        print("I am from constructor")

    def printInfo(self):
        print(self.name1,self.age1)

st1=Student2("Sohag",45)
st2=Student2("Lobid",25)
st1.name1="Tofayel"

print(st1.school)
print(st1.name1)
print(st2.school)
print(st2.name1)




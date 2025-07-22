#variable is declared and intialized when created
name="Sohag" #global
age=45#int
gpa=4.5#flat
print(type(name))#str
print(type(age))#int
print(type(gpa))#int
print(4)#print() built-in method
print(name)#print() built-in method

#funct
def printInfo():
   # global phone #add global phone to make global
    name="Rani" #local
    phone=349739447 #local
    print(name)
print("----------------------")
def printInfo2():
    print(name)

printInfo()
printInfo2()
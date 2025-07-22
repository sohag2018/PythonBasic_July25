#zero parameter
def add():
    print(5+6)
add()

#1 parameter
def add1(num):
    print(num+6)
add1(50)

#2 parameter
def add1(num1,num2):
    print(num1+num2)
add1(50,20)

print("Default parameter value")#if you dont pass then it will take default
def print_country(country="Bangladesh"):
    print(country)
print_country()

print("Arbitrary argument/*args")#if you dont know the number of parameter
def addNumber(*num):
   return sum(num)
sum=addNumber(5,2,2)
print(sum)

print("keyword argument")#you explicitly assign pass parameter along with value
def addNumber1(num1,num2):
    return num1+num2
sum=addNumber1(num1=5,num2=20)
print(sum)


print(" **kwargs")#when you dont know how many keyword you will send
def addNumber2(**person):
    for p in person:
        print(person[p])
addNumber2(fname="Muhammad", lastname="Sohag")

print(" **Keyword-Only")
def printName(*,name):
    print(name)
printName(name="Muhammad")

print("Positional-Only-----------")
def printAge(age, / ):
    print(age)
printAge(45)

#------------

def print_my_name(name):
    return print(f"My name is {name}")
print_my_name("Sohag")
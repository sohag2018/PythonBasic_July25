class Student:
    #constructor
    def __init__(self,f_name,l_name):
        self.firstname=f_name
        self.lastname=l_name

    #instance method
    def printInfo(self):
        print(self.firstname,self.lastname)

    @classmethod
    def printClass(cls,full_name):
        nameparts=full_name.split()#spliting into array [Noyon][Sarker]
        if len(nameparts)==2:
            return cls(nameparts[0],nameparts[1])
        else:
            raise ValueError("You have entered wrong format")


st2=Student.printClass("Noyon Sohag")
st2.printInfo()

# st1=Student("Noyon","Sarker")
# st1.printInfo()


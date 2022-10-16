'''
INHERITANCE

1. Single
2. Multiple
3. Multilevel

In case of ambiguity, Classes inherited first will be given priority
so its attribute and methods will be choosen 

In case of Multilevel, Nearest Parent will be given priority
'''
class Freelancer:
    company = "WFH"

class Employer:              #Base class
    company = "Google"

    def __init__(self,name):  #Para const
        self.name = name

    def getInfo(self):
        print(f"Welcome {self.name} in {self.company}")

    @staticmethod  #Static method
    def greet():
        print("Hello World")


class Programmer(Employer,Freelancer):  #Derived class
    language = "Python"
    company = "YouTube"
    def getLang(self):
        print(f"Language is {self.language}")

    def getInfo(self):   #Overriding getInfo()
        print(f"Welcome {self.name} in {self.company}")


Pratik = Employer("Pratik")
Employer.greet()
Pratik.greet()
Pratik.getInfo()

Pratik.company="Microsoft"



Employer.company = "Amazon"

print(Pratik.company)
print(Employer.company)
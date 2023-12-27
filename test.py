
class Animal:
    id = 11
    def __init__(self,age,name="DUNKI",gender="N/A",):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduction(self):
        print(f"Mero name {self.name} ho, ma {self.age} ko vaye..,")

a = Animal(30,name="DOLPHIN")
b = Animal(15,gender='MALE')

class Mammal(Animal):
    def introduction(self):
        print(f"Mero name {self.name} ho, ma {self.age} ko vaye.., ma euta Mammal ho")
    
mammal = Mammal(16,"JANAKI",gender="FEMALE")
mammal.introduction()


print(a.id)
print(a.name)
print(a.age)
print(a.gender)
print('calling the method')
a.introduction()
print("this is data from b")
print(b.name,b.age,b.gender)


#Operator overloading

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __gt__(self,other):
        return True if self.age > other.age else False
    
dog1 = dog('Bolt',10)
dog2 = dog('Lucy',11)

print(dog2 > dog1)

print(dog1.age)
print(type(dog1))
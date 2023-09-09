# An object is an instance of a class
# A class is a type of object

class Animal:
    def walk(self):
        print("I can walk")



class dog(Animal):

    def __init__(self,name,age): # init is a special type of method (constructor)
        self.name = name
        self.age = age


    def bark(self):   # self is an argument of a method which points to the current object instance
        return 'Woof!'


Dog1 = dog('Bolt',10)
print(type(Dog1)) #__main__.dog

print(Dog1.name)
print(Dog1.age)

print(Dog1.bark())
Dog1.walk()
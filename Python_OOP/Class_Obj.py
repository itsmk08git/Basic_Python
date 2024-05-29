class Person:
    def  details(self):
        print("Name: Mohan\n Rollno:2")

person1=Person()
person1.details()

'''
    :__init()__
          -It is a special method in Python.
          -It is automatically called when an object is created form a class.
          - Used to initialized the attributes of the object.
          -Also known as a constructor.
'''
class Computer:
    def __init__(self, cpu, ram):
        self.cpu= cpu
        self.ram=ram

    def display(self):
        print("The Model is ", self.cpu, self.ram)
        print(f"The Model is Acer {self.cpu} {self.ram}")

comp1 =Computer("Ryzen 5", 512)
comp1.display()

'''
    :__str()__
         -It controls what should be returned when the
             class object is represented as string.
         -If it is not set then memory address of the object will be represented(i.e, hex value).
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


  def __str__(self):
    return f"Name:{self.name}\nAge:{self.age}"


p1 = Person("John", 36) #object created
print(p1)

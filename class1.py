class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#method #2
    def printname(self):
        print(self.name, self.age)

#3
class Student(Person):
    pass

#4
class Student2(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = 2021

#method
    def welcome(self):
         print(self.year)

#1
p1 = Person("Jenny",30)
print(p1.name)
print(p1.age)

#2
x = Person("John",36)
x.printname()

#3
y = Student("Miki",15)
y.printname()

#4
z = Student2("Agnes",20, 2019)
z.printname()
z.welcome()

#C:\Users\lcg\AppData\Local\Programs\Python\Python38-32\Scripts
#pip


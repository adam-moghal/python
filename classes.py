# class Student:
#     def __init__(self,name,age,year):
#         self.name = name
#         self.age = age
#         self.year = year

#     def displayStudent(self):
#         return("Student name is " + self.name + " age is " + str(self.age) + " and is in " + self.year)

# student1 = Student("Adam",16,"College first year")

# print(student1.displayStudent())

# inheritence

class Parent:
    counter = 10
    def __init__(self):
        print("class initialised")
    def parentFunction(self):
        print("Parent function is being called")
    def setCounter(self,num):
        Parent.counter = num
    def showCounter(self):
        print(str(Parent.counter))



class Child(Parent):
    def __init__(self):
        print("Child class is being initialised")

    def childFucntion(self):
        print("child class being called")


c = Child()
c.childFucntion()
c.parentFunction()
c.showCounter()
c.setCounter(12123)
c.showCounter()
# what is oop?
# oop is a programming paradigm that uses objects
# and their interactions to design and program applications.

# what is an object?
# an object is a software bundle of related state and behavior.

# what is a class?
# a class is a blueprint for creating objects.

# what is a method?
# a method is a behavior that an object can perform or function.

# what is an attribute?
# an attribute is a piece of data stored in an object or variable.


# how to create a class?
# class ClassName:
#     pass

# what is instance?
# an instance is a specific object created from a particular class.


# class Student:
#     name = "John"
#
#     def student_info(self):
#         print("This is a student info method")
#
#
# obj = Student()
# print(obj.name)
# obj.student_info()


# class Student:
#     name = "John"
#
#     # def test(self):
#     #     return "This is a test method"
#
#     def student_info(self, sid, age, phone):
#         print(sid, age, phone)
#         # sObj = Student()
#         # print(sObj.name)
#         # print(self.test())
#
#
# obj = Student()
# # print(obj.name)
# obj.student_info(1, 20, 1234567890)


# class SPI:
#     def take_value(self):
#         p = int(input("Enter the principle amount: "))
#         t = int(input("Enter the time: "))
#         r = int(input("Enter the rate: "))
#         return [p, t, r]
#
#     def calculate(self):
#         p, t, r = self.take_value()
#         si = (p * t * r) / 100
#         return si
#
#     def display(self):
#         return f"The simple interest is: {self.calculate()}"
#
#
# obj = SPI()
# print(obj.display())

# what is constructor?
# a constructor is a special method that is used to
# initialize the object of a class.


# class Student:
#
#     def __init__(self,name,age):
#         print("This is a constructor")
#
#     # @property
#     # @staticmethod
#     # @classmethod
#     def info(self):
#         print("This is a student info method")
#
#     def __str__(self):
#         pass
#
#     def __repr__(self):
#         pass
#
#     def __del__(self):
#         print("This is a destructor")
#
#
# obj = Student()
# obj.info()

# data =['ram']
# print(type(data))

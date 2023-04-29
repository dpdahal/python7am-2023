# def zero_check(any_function):
#     def inner_function(x, y):
#         if x == 0 or y == 0:
#             return "Sorry, Zero is not allowed"
#         else:
#             return any_function(x, y)
#     return inner_function
#
# @zero_check
# def add(x, y):
#     return x + y
#
#
# print(add(100,0))
#
#


# class Student:
#     __name = ''#
#     @property
#     def get_name(self):
#         return self.__name
#
#     @get_name.setter
#     def get_name(self, name):
#         self.__name = name
#
#     @get_name.deleter
#     def get_name(self):
#         del self.__name
# obj  = Student()
# obj.get_name='hari'
# print(obj.get_name)
# del obj.get_name


#
# class Students:
#     __name=''
#     __roll_no=''
#
#     @property
#     def get_name(self):
#         return self.__name
#
#     @get_name.setter
#     def get_name(self, name):
#         self.__name = name
#
#     @get_name.deleter
#     def get_name(self):
#         del self.__name
#
#     @property
#     def get_roll_no(self):
#         return self.__roll_no
#
#     @get_roll_no.setter
#     def get_roll_no(self, roll_no):
#         self.__roll_no = roll_no
#
#     @get_roll_no.deleter
#     def get_roll_no(self):
#         del self.__roll_no
#
# obj = Students()
# obj.get_name = 'hari'
# obj.get_roll_no = 1
# print(obj.get_name)
# print(obj.get_roll_no)
# del obj.get_name
# del obj.get_roll_no
#
# print(obj.get_name)
# print(obj.get_roll_no)

# what static method?
# static method is a method which is not related to class or instance


# class Student:
#
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#
#     @staticmethod
#     def get_name():
#         return Student.name
#
#
# print(Student('ram',30).get_name())
# obj = Student()
# print(obj.get_name())


# what is class method?
# class method is a method which is related to class
# but not related to instance

# class Student:
#
#     @classmethod
#     def get_name(cls):
#         print("This is a class method")
#
#
# Student.get_name()

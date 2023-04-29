# class Laptop:
#     _price = 10
#
#     def brand(self, name):
#         print("Brand Name:", name)


# class Dell(Laptop):
#
#    def get_price(self):
#        return self._price
#
# obj = Dell()
# print(obj.get_price())
#
# class MI(Laptop):
#     pass
#
# obj = Dell()
# obj.brand("Dell")


# class Laptop:
#     __price= 20000
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, new_price):
#         self.__price = new_price
#
# obj = Laptop()
# obj.set_price(30000)
# print(obj.get_price())


# class Student:
#
#     def __new__(cls, *args, **kwargs):
#         print("New method called")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("Init method called")
#
#     def __del__(self):
#         print("Del method called")
#
#
# obj = Student()


# class Student:
#     name = 'ram'
#
#     def students_info(self):
#         print("Students Info")
#
#     def __str__(self):
#         return self.name
#
#
# obj = Student()
# print(obj)



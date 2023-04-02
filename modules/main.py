# what is modules?
# Modules are files containing Python definitions and statements.

# types of modules
# 1. built-in modules: datetime, math, random, os, sys, etc.
# 2. user-defined modules: created by the user

# import module
# import lib.students
#
# print(lib.students.add_students())

# from lib import *
#
# print(students.add_students())
# print(users.get_users())

# from lib.users import *
#

# print(add_students())
# print(show_students())

# import datetime

# bDate = str(datetime.date(2023, 8, 4))
# y= bDate.split("-")
# print(y)
# print(bDate)
# print(bDate.strftime("%A/%B/%Y"))
# today = datetime.date.today()
# print(bDate-today)

# jobs = [
#     {'id': 1, 'title': 'Python ', 'expire_date': '2023-05-10'},
#     {'id': 2, 'title': 'Java ', 'expire_date': '2024-07-10'},
#     {'id': 3, 'title': 'C# ', 'expire_date': '2020-08-10'},
# ]
# import os
# import sys

# datetime.datetime(2020, 1, 2)
# print(datetime.date.today())
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)
# print(dir(datetime))


# import sys

# print(dir(sys))
# print(sys.argv)

# import os

# print(os.path.exists('demo1.txt'))

# os.mkdir("test")
# os.rmdir("test")
# os.rename("test", "test1")
#
# obj = open('students.txt', 'a')
# obj.write("Hello python")
# obj.write('\n')
# obj.close()
# name
# email
# address

# obj = open('students.txt', 'r')
# print(obj.read())
# print(obj.readline())
# print(obj.readlines())
# obj.close()

# with open('students.txt', 'a') as obj:
#     name = input("Enter name: ")
#     email = input("Enter email: ")
#     address = input("Enter address: ")
#     obj.write(f"{name},{email},{address}")
#     obj.write('\n')
#
#
# with open('students.txt', 'r') as sObj:
#     data = sObj.readlines()
#     for line in data:
#         print(line.split(','))


def register():
    # username
    # password
    pass

def login():
    # username
    # password
    pass
# what is function?
# function is a block of code which only runs when it is called.
#
# types of function
# 1. built-in function: print(), input(), type(), len(), etc.
# 2. user-defined function: function which is created by user.
#
# how to create a function?
# def function_name():
#     code
#     code
# call the function
#
# case: user_name
#
# def welcome():
#     print('welcome to python')
#
#
# welcome()
#
#
# function with parameter
#
#
# def welcome(name, price):
#     print(f'welcome to {name} price is {price}')
#
#
# welcome('python', 1000)
# welcome('java', 2000)
# welcome('c++', 3000)
#
#
# function with optional parameter
#
#
# def welcome(name, price=0):
#     print(f'welcome to {name} price is {price}')
#
#
# welcome('python',2000)
# welcome('java')
#
# def welcome(course):
#     print(course)
#
# welcome(['python','java','c++','nodejs'])
#
# *a,b =10,20,304,50
#
# *args: []
# def welcome(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# welcome('python', 'java', 'c++', 'nodejs', name='python', price=1000)
#
#
# function return value
#
# def welcome():
#     return 'welcome to python'
#
#
# print(welcome())
#
# def add_sub(a, b):
#     c = a + b
#     d = a - b
#     return [c, d]
#
#
# x, y = add_sub(10, 5)
#
# def welcome():
#     return "hello"
#
#
# print(welcome())
#
# function scope
#
# global scope: outside the function call everywhere
# local scope: inside the function call only inside the function
#
# x = 10
#
#
# def test():
#     print(x)
#
#
# test()
#
#
# def test():
#     x = 10
#
#     print(x)
#
#
# test()
#
#
# x = 10
#
#
# def test():
#     global x
#     x = x + 90
#     print(x)
#
#
# test()
# print(x)
#
#
# lambda function: anonymous function
#
# a = lambda x, y: x + y
# print(a(10, 20))
#
#
# def test():
#     print("Hello World")
#     test()
#
#
# test()
#
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
#
#
# print(fac(6))
# 5-1: 4 * 5: 20
# 4-1: 20 * 3: 60
# 3-1: 60 * 2: 120
# 2-1: 120 * 1: 120
#
# def a():
#     return 10
#
#
# def b():
#     print(a())
#
#
# b()
#
# p,t,r
#
# def take_value():
#     p = int(input("Enter the principle amount: "))
#     t = int(input("Enter the time: "))
#     r = int(input("Enter the rate: "))
#     return [p, t, r]
#
#
# def calculator():
#     p, t, r = take_value()
#     return p * t * r / 100
#
#
# def display():
#     return f"Simple interest is {calculator()}"
#
#
# print(display())
#
#
# nested function
#
# def outer():
#     def inner(name):
#         return f"Hello {name}"
#
#     return inner
#
#
# res = outer()
# print(res('ram'))

# WAP to make total function
# 1,2,3,4,5,6,7,8

# def total(*args):
#     sum_number = 0
#     for i in args:
#         sum_number = sum_number + i
#     return sum_number
#
#
# print(total(1, 2, 3, 4, 5, 6, 7, 8))

# WAP to enter any data and return the data type

# def data_type(data):
#     return type(data)

# def even_odd(args):
#     even = 0
#     odd = 0
#     for i in args:
#         if i % 2 == 0:
#             even = even + 1
#         else:
#             odd = odd + 1
#     return f"Even: {even} Odd: {odd}"
#
#
# data = []
# for a in range(1, 5):
#     data.append(int(input("Enter the number: ")))
#
# print(even_odd(data))


# modules

# def connection():
#     """
#     This function is used
#     to connect to the database
#     """
#     return "Database connected"

# print(connection.__doc__)
# print(connection.__name__)

# print(__file__)

print(__name__)
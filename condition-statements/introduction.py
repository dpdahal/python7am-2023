# control statements
# if, elif, else,nested if esle

# x = 50
# y = 300
# z = 200
#
# if x > y and x > z:
#     print("x is greater than y and z")
# elif y > x and y > z:
#     print("y is greater than x and z")
# else:
#     print("z is greater than x and y")

# num = 5
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# WAP to check enter any number is divisible by 3 and 5 or not

# num = int(input("enter any number: "))
#
# if num % 3 == 0 and num % 5 == 0:
#     print("divisible by 3 and 5")
# else:
#     print("not divisible by 3 and 5")

# nepali = int(input("enter nepali marks: "))
# english = int(input("enter english marks: "))
# math = int(input("enter math marks: "))
# science = int(input("enter science marks: "))
# social = int(input("enter social marks: "))
# total = nepali + english + math + science + social
# percentage = total / 5
#
# if percentage >= 35 and percentage <= 45:
#     print("third division")
# elif percentage >= 45 and percentage <= 60:
#     print("second division")
# elif percentage >= 60 and percentage <= 75:
#     print("first division")
# elif percentage >= 75 and percentage <= 100:
#     print("distinction")
# else:
#     print("fail")

# print("1. Dell 2. HP 3. Lenovo")
# question = int(input("select any option: "))
#
# if question == 1:
#     print("Dell")


userName = 'admin'
password = 'admin123'

# user = input("enter username: ")
# passw = input("enter password: ")
#
# if user == userName:
#     if passw == password:
#         print("login successfully")
#     else:
#         print("password is incorrect")
# else:
#     print("username is incorrect")

# x = 50
# y = 300
# z = 200
# elif, and or not only if else

# if user == userName and passw == password:
#     print("login successfully")
# else:
#     print("username & password is incorrect")

# x = 50
# y = 30
# z = 200
#
# if x > y:
#     if x > z:
#         print("x is greater")
#     else:
#         print("z is greater")
# else:
#     if y > z:
#         print("y is greater")
#     else:
#         print("z is greater")


x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
if x > y:
    if x > z:
        print(x, z, y)
    else:
        print(z, x, y)
else:
    if y > z:
        print(y, z, x)
    else:
        print(z, y, x)

# if x > y:
#     print(x)
#     print(y)
# else:
#     print(y)
#     print(x)

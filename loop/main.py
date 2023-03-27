# for,while,nested loop
# for loop: list tuple set dictionary
# while loop: condition

# data = ['ram', 'shyam', 'hari', 'gita', 'sita']
# print(data[0])

# for name in data:
#     print(name)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]
# # total even
# # total odd
# total_even = 0
# total_odd = 0
# for number in numbers:
#     if number % 2 == 0:
#         total_even += 1
#     else:
#         total_odd += 1
#
# print(total_even)
# print(total_odd)

# users = [
#     ['ram', 'sita', 'hari'],
#     ['gita', 'sita', 'hari'],
#     ['ram', 'sita', 'hari']
# ]
#
# for names in users:
#     for a in names:
#         print(a, end=',')

# names = []
# num = int(input('Enter a number: '))
# for i in range(1, num + 1):
#     name = input('Enter a name: ')
#     names.append(name)
#
# for name in names:
#     print(name)

# x = 1
#
# while x <= 10:
#     print(x)
#     x += 1

# num = int(input("Enter any number: "))
# x = 1
# studentsMark = []
# while x <= num:
#     print(f"========Student {x} =========")
#     for a in range(1):
#         nepali = int(input("Enter Nepali marks: "))
#         english = int(input("Enter English marks: "))
#         science = int(input("Enter Science marks: "))
#         social = int(input("Enter Social marks: "))
#         math = int(input("Enter Math marks: "))
#         mark = [nepali, english, science, social, math]
#         studentsMark.append(mark)
#     x += 1


# print(f"student roll no. 1 total marks per subject: ")

# enter number of times
# 7

# 1
# 2
# 1
# 2
# 5

# break, continue

# 1-10
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total_even = 0
# total_odd = 0
#
# x = 1
# while x <= len(a):
#     if a[x] % 2 == 0:
#         total_even += 1
#     else:
#         total_odd += 1
#     x += 1

# for x in a:
#     if x % 2 == 0:
#         total_even += 1
#     else:
#         total_odd += 1

# 1,1,2,3,5,8,13,21,34,55


# x = 1
#
# while x <= 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1

# x = 0
# while x <= 10:
#     if x == 5 or x == 7:
#         x += 1
#         continue
#     print(x)
#     x += 1

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print('====================')

users = [
    {'username': 'ram', 'password': 'ram002'},
    {'username': 'admin', 'password': 'admin002'},
    {'username': 'hari', 'password': 'hari002'}
]

username = input('Enter username: ')
password = input('Enter password: ')
login_success = False

for user in users:
    if username == user['username'] and password == user['password']:
        login_success = True

if login_success:
    print(f'Welcome {username}')

else:
    print('Invalid username or password')

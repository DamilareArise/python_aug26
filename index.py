# print("Helloo... How you doing?")
# print(23 + 1)

# commenting
# 1. single line comment
"""
2. Multi line or block comment / doc string

"""

# print("""
#     1. Buy Data
#     2. Check balance
#     3. Exit
# """)


# indentation 

def hello():
    print('Helloo')
    
    
# Python variables 
student = "Moni"
balance = 2950.50

# 1. variable name
# 2. Assignment operator
# 3. Value

# print(student)

# Laws guiding variable declaration
# 1. variable names can only start with an alphabet or underscore
# 2. variable names should not contain space
# 3. Variable name must be descriptive
# 4. A variable name can only contain alphabet, numbers and underscore

# Casing method
# i. Camel casing. 
firstNameOfTheStudent = "Kelly"
# ii. Pascal casing
FirstNameOfTheStudent = "Kelly"
# iii. Snake casing
first_name_of_the_student = "kelly"


# Types of variable declaration
# 1. single variable single value.
first_name = "Damilare"
# 2. single variable multiple value
students = "Moni", "Temi", "Kelly"
# print(students)
# 3. multiple variables single value 
x = y = z = 5
x = 10
# print(x)
# 4. multiple variable multiple value
x, y, z = 10, 20, 30
# print(z)

# Concatenation
# print("Hello" + "World")
first_name = "Damilare"
last_name = "Arise"
age = 20
account_balance = 5000.5

# print("Welcome to class "+ first_name)
# print("My name is "+ last_name +" "+ first_name)
# print("I am "+ str(age) + "years old")
# print("Your balance is #"+str(account_balance))

# using comma
# print("Welcome to class", first_name)
# print("My name is", last_name, first_name)
# print("I am", age, "years old")

# F-string
# print(f"Welcome to class {first_name}")
# print(f"My name is {last_name} {first_name}")
# print(f"I am {age}years old")
# print(f"Your balance is #{account_balance}")


# first_name = input("Firstname: ")
# first_name 

# print(f"Welcome to class {first_name}")


    
# DATATYPES
# 1. Text Type / strings. it is denoted by "" or ''. str() is the object for strings
# 2. Number types
    # i. Integers - int() e.g 12, 230
    # ii. Float - float() e.g 1.5, 23.455
    # iii. complex - complex() e.g 2 + 3j
    
# 3. Sequence Type:
    # i. tuple - tuple(), e.g  (1, 2, 4, 5)
    # ii. list - list(), e.g [1, 2, 3, 4]
    # iii. range - range()
    
# students = ('Ayo', 'Ola', 'Lola')

# students = ['Ayo', 'Ola', 'Lola']
# students
# print(type(students))

# print(list(range(20)))
# print(list(range(1, 21)))
# print(list(range(1, 21, 2)))


# 4. Boolean type: True and False
isActive = True

# 5. Set type : set(), {1, 2, 3}
setA = {1, 2, 3, 4, 6, 10, 9, 8, 7, 7}
names = {'Ayo', 'Ola', 'Lola', 'Ayo'}
# print(names)

# 6. Mapping type:  dict(), {"name": "Ayo", 'age': 20}

# student = {"name": "Ayo", 'age': 20}

# 7. None type 
box = None

# 8. Binary types : Byte, btyearray, memoryview 


# Datatypes conversion

num = 12
# print(str(num))

# amount = float(input("Amount: "))
# print(type(amount))


# python operators
# 1. Arithmetic operators: +, -, /, *, **, %, //
# print(5 ** 2)
print(5 % 2)
# print(5 // 2)

# 2. Assignment operators: =, +=, -=, /=, *= ...
# x = 5
# x += 2  # x = x + 2
# x -= 2
# print(x)

# 3. comparison operator: ==, !=, >, <, >=, <=
x = 2
# print(x >= 2)

# 4. Logical Operator: or, and , not
""" 
A --- B --- AND --- OR
0     0     0       0
0     1     0       1
1     0     0       1
1     1     1       1

NOT A
1
1
0
0

"""

email_is_verified = False
password_is_verified = False
# print(email_is_verified and password_is_verified)


# conditional statement (if/else/elif)

x = 5

# if x == 3:
#     print('yes!')
# else:
#     print("Oh no !")


# if email_is_verified:
#     print("Access Granted.")
# else:
#     print("Wetin you dey find")

# if email_is_verified and password_is_verified:
#     print("Login Successful")
# else:
#     print("Incorrect email or password")

# original = 3
# predicted_score = int(input("Predicted score: "))

# if predicted_score == original:
#     print('you won 100k')

# elif predicted_score > 2:
#     print("You tried, you won 10k")
    
# else:
#     print("Sorry oh! you gat nothing")

# fizz - divisible by 3 with no remainder
# Buzz - divisible by 5 with no remainder
# fizzBuzz - divisible by 3 and 5 with no remainder 

number = int(input("Number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is a FizzBuzz")

elif number % 3 == 0:
    print(f"{number} is a Fizz")
    
elif number % 5 == 0:
    print(f"{number} is a Buzz")

else:
    print(f"{number} is neither Fizz nor Buzz")
    
    
# build a system that tells if a number is odd or even
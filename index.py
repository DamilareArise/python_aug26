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


first_name = input("Firstname: ")

print(f"Welcome to class {first_name}")


    
# DATATYPES
# 1. Text Type / strings. it is denoted by "" or ''. str() is the object for strings
# 2. Number types
    # i. Integers - int() e.g 12, 230
    # ii. Float - float() e.g 1.5, 23.455
    # iii. complex - complex() e.g 2 + 3j
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
# print(5 % 2)
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
A --- B --- AND --- OR --- XOR
0     0     0       0       0
0     1     0       1       1
1     0     0       1       1
1     1     1       1       0

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

# number = int(input("Number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print(f"{number} is a FizzBuzz")

# elif number % 3 == 0:
#     print(f"{number} is a Fizz")
    
# elif number % 5 == 0:
#     print(f"{number} is a Buzz")

# else:
#     print(f"{number} is neither Fizz nor Buzz")
    
    
# build a system that tells if a number is odd or even


# 5. Identity operator: is, is not
x = 5
y = 5
# print(x is not y)

# 6. Membership operator: in, not in

students = ['Ade', 'Ola', 'Dami']
student = 'Folakemi' #['F', 'o', 'l'..]
# print(student not in students)

# A simple email validator

# email = input("Email: ")

# if '@' in email and '.' in email:
#     print(f"{email} is a valid email.")

# else:
#     print("Invalid email")
    

# 7. bitwise operator 
# & - and 
# | - or
# ~ - not
# ^ - xor

x = 10
y = 5
# print(~x)
# print(bin(y))
# print(bin(x ^ y))

""" 
1   0   1   0
    1   0   1
1   1   1   1

"""



# Python strings 

name  = 'Ayo' # ['A', 'y', 'o']

# print(ord('a'))
# print(name[-1])
# print(len(name))

exp = "  Hi Everyone, Python is my favorite programming language.  "
# print(len(exp))
# print(exp[3:11])
# print(exp[3:])

# print(exp.upper())
# print(exp.lower())
# print(exp.capitalize())
# print(exp.title())

# print(len(exp.strip()))

# action = input("Are you sure? Yes/No: ")
# if action.strip().lower() == 'yes':
#     print('Proceed')

# else:
#     print('Decline')
    
# 1. Build a simple grading system
# 70 - 100  = A
# 60 - 69 = B
# 50 - 59 = C
# 45 - 49 = D
# 40 - 44 = E
# 0 - 39 = F

# 2. Build a simple CBT app. 


# Python collections or array
# 1. list: it can be indexed, changeable, allows duplicate items, ordered 
# [] or list()
basket = ['Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish', 'apple']
# print(type(basket))
# print(basket[-1])
# print(basket[0:4]) #slicing
# basket[3] = 'Egg'

# basket.append('Egg')
# basket.insert(3, 'Egg')
# basket.extend(["Egg", 'Oil'])
# basket.pop(2)
# basket.remove('Meat')
# basket.clear()

# print(basket.index('Fish', 4))
# print(basket.count('Fish'))

# basket.sort(key=str.lower, reverse=True)
# print(basket)

# scores = [12, 14, 16]
# print(sum(scores))
# print(max(scores))


# 2. tuple: indexed, allows duplicate, ordered, unchangeable
# () or tuple()

basket = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# print(type(basket))

# print(basket[0])
# basket[0] = "Apple"

# print(basket.count("Fish"))
# print(basket.index("Meat"))

# new_basket = list(basket)
# print(new_basket)
# new_basket[0] = "Apple"
# basket = tuple(new_basket) 
# print(basket)

# unpacking

# a, b, c, d, e, f = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# a, b, *c, f = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# *a, b = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')

# *a, = ('Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish')
# print(a)


# 3. set: unordered, doesn't allow duplicate, unchangeable, can't be indexed
# {} or set()

basket = {'Orange', 'Tomatoes', 'Meat', 'Fish', 'Pepper', 'Fish'}
# print(basket[0])
# basket[0] = "Apple"

# basket.add('Apple')
# basket.update(["Apple", "Egg"])
# basket.pop()
# basket.remove('Fisherman')
# basket.discard('Fisherman')
# print(basket)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {2, 4, 10, 12, 11}
setC = {1, 2, 3, 4}

# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setB.difference(setA))
# print(setA.symmetric_difference(setB))

# setA.symmetric_difference_update(setB)
# print(setA)

# print(setA.issubset(setC))



# 4. dictionary 
# {key:value} or dict()
car = {
    "brand": "Toyota",
    "model": "Camry 2026",
    "color": "wine",
    "type": "hybrid",
    # "owner": {
    #     "name": "Monioluwa",
    #     "address": {
    #         "state": "Oyo state",
    #         "country": "Nigeria"
    #     }
    # }
}

# print(car['types'])
# print(car['owner']['address']['country'])
# owner = car['owner']
# print(owner['address']['country'])

# print(car.keys())
# print(car.values())
# print(car.items())

# print(car.get('type', "Not Found"))
# car.pop('type')
# car.popitem()

# car.update({"model": "Camry 2027"})
# car['model'] = "Camry 2027"

# print(car)


# Python Loop
# 1. For loop: it iterate over a sequence(e.g list, tuple, set, or string)

# name = "Monioluwa"
# for x in name:
#     print(x)
#     print("_______")
    
# students = ["Ade", "John", "Ola"]
# for student in students:
#     print(f"Welcome to class {student}")
    

# score = 0
questions = [
    "What is the capital of Lagos a. Ikeja b. Iyanapaja",
    "What is the capital of Edo a. Ikeja b. Benin",
    "What is the capital of Osun a. Osogbo b. Iyanapaja",
]
answers = ["a", "b", "a"]
marks = [10, 20, 5]

# x = 1

# for ques, ans, mark in zip(questions, answers, marks):
#     print(f"{x}. {ques}")
#     x+=1
    
#     # marking scheme
#     user_ans = input("Ans: ")
#     if user_ans.strip().lower() == ans:
#         print("Correct")
#         score += mark
#     else:
#         print("Incorrect")

# print(f"Total score: {score}/{sum(marks)}")



# exam = [
#     ("What is the capital of Lagos a. Ikeja b. Iyanapaja", "a", 10),
#     ("What is the capital of Edo a. Ikeja b. Benin", "b", 20),
#     ("What is the capital of Osun a. Osogbo b. Iyanapaja", "a", 5)
# ]


# # a, b, c=("What is the capital of Lagos a. Ikeja b. Iyanapaja", "a", 10)

# no = 1
# for ques, ans, mark in exam:
#     print(f"{no}. {ques}")
#     no+=1
    
#     user_ans = input("Ans: ")
#     if user_ans.strip().lower() == ans:
#         print("Correct")
#         score += mark
#     else:
#         print("Incorrect")
        
# print(f"Total score: {score}/{sum(marks)}")


# exam = {
#     "What is the capital of Lagos a. Ikeja b. Iyanapaja": "a",
#     "What is the capital of Edo a. Ikeja b. Benin": "b",
#     "What is the capital of Osun a. Osogbo b. Iyanapaja": "a"
# }

# print(exam.items())

# for ques, ans in exam.items():
#     print(ans)

  
# students = ["Ade", "John", "Ola"]
# for student in students:
#     print(student)  
#     for letter in student:
#         print(letter)


# for x in range(1, 6):
#     print(f"{x} Times Table")
#     for y in range(1, 6):
#         print(f"{x} x {y} = {x*y}")
    
    

# 2. While loop: While keeps iterating as long the condition is True.

# x = 10
# while x > 0:
#     print(x)
#     x -= 1
    
    
# balance = 1000
# while balance > 100:
#     balance -= 100
#     print("You can still buy stuff, balance is", balance)
    
#     if balance == 500:
#         print("I no dey buy again")
#         break
    
     

# ticket = 10
# while ticket > 0:
#     age = int(input("Age: "))
#     if age < 18:
#         print("Access not granted")
#         continue
    
#     ticket -= 1
#     print("Ticket remains", ticket)

x = 10

# while True:
#     x -= 1
#     print(x)
#     if x == 4:
#         break


# A simple Todo app

database=[]

while True:
    print("""
    1. Add a todo
    2. Delete a todo
    3. Edit a todo
    4. View all
    5. Clear all
    6. Set todo as completed
    #. exit
    """)
    choice = input("Choice: ").strip()
    if choice == '1':
        print('Add Todo')
        todo = input("Your Todo: ").strip().capitalize()
        if todo:
            database.append(todo)
            print("Todo saved.")
        else:
            print("No todo added.")
        
    elif choice == "2":
        print("Delete Todo")
        item_no = int(input("Delete Item no: "))
        
        if item_no > len(database):
            print("Invalid Item no. Try again.")
            continue
        
        index = item_no - 1
        database.pop(index)
        print("Todo Deleted.")
    
        
    elif choice == "3":
        print("Edit Todo")
        item_no = int(input("Edit Item no: "))
                
        if item_no > len(database):
            print("Invalid Item no. Try again.")
            continue
        
        
        new_name = input("New: ").strip().capitalize()
        if not new_name:
            print("Todo can't be empty")
            continue
        
        index = item_no - 1
        database[index] = new_name
        print("Todo edited successfully")
        
        
        
    elif choice == "4":
        print("View all Todo")
        
        no = 1
        for todo in database:
            print(f"{no}. {todo}")
            no+=1
        
    elif choice == "5":
        print("Clear all Todo")
        
        database.clear()
        
        
    elif choice == "#":
        # exit("Goodbye!")
        break
   
    else:
        print("Invalid input")
        
        
# .pop , .append, .update, .extend


# value1= float(input("Value 1: "))
# value2= float(input("Value 2: "))

# print("""
#     1. Addition
#     2. Subtraction
#     3. Division
#     #. Exit     
# """)

# choice = input("choice: ").strip()
# if choice == "1":
#     print(f"Ans: {value1 + value2}")
# elif choice == "2":
#     print(f"Ans: {value1 - value2}")
# elif choice == "3":
#     print(f"Ans: {value1 / value2}")
# elif choice == "#":
#     exit('Goodbye !')
# else:
#     print("Invalid option")


# ussd app - conditional statement
# simple banking system - conditional statement, operators, data structure
# bet app - set, conditional, loop


# deposit, withdraw, create account, login, check balance, 


database = []

while True:
    print("""
        1. Create Account
        2. Login
        #. Exit      
    """)
    
    choice = input("Choice: ").strip()
    if choice == "1":
        fullname = input("Fullname: ").strip().title()
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()
        confirm_password = input("Confirm Password: ").strip()
       
        if not fullname or not email or not password or not confirm_password:
            print("❌All fields are required")
            continue
        
        if password != confirm_password:
            print("❌Password doesn't match")
            continue
        
        user = {
            "fullname": fullname,
            "email": email,
            "password": password,
            "balance": 0.0
        }
        database.append(user)
        print("Registration successfull") 
           
       
    elif choice == "2":
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()
        active_user = None
        
        
        for user in database: # [{}, {}, {}]
            if user['email'] == email:
                active_user = user 
        
        if not active_user or active_user['password'] != password:
            print("Invalid email or password")
        else:
            print("Login successfull")
            while True:
                print("""
                1. Deposit
                2. Withdraw
                3. Check balance
                #. Logout   
                """)
                
                choice = input("Choice: ").strip()
                if choice == "1":
                    # print(active_user)
                    amount = float(input("Amount: "))
                    if amount < 1:
                        print("Amount can't be less and #1.")
                        continue
                    
                    active_user['balance'] += amount
                    print(f"You've deposited #{amount}. Your account balance is #{active_user['balance']}")
                    
                    # print(database)
                    
                elif choice == "2":
                    amount = float(input("Amount: "))
                    if amount < 1:
                        print("Amount can't be less and #1.")
                        continue
                    
                    if amount > active_user['balance']:
                        print("Insufficient funds")
                        continue
                    
                    active_user['balance'] -= amount
                    print(f"You've withrawn #{amount}. Your account balance is #{active_user['balance']}")
                    
                elif choice == "3":
                    print(f"Your account balance is #{active_user['balance']}")
                elif choice == "#":
                    print("Signing out...")
                    break
                else:
                    print("Invalid choice.")
        
    elif choice == "#":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")
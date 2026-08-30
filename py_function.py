# 1. Declaration stage
# 2. Definition stage
# 3. invocation stage


def add_todo():
    # logic
    print("Todo added!")
    
# add_todo()

# create a function that calculate the area of a circle
def area_of_circle():
    radius = float(input("Radius: "))
    aoc = 3.142 * (radius**2)
    print(f"AOC: {aoc}cm^2")
    
# area_of_circle()



def USSD():
    code = input("USSD: ")
    if code == "*312#":
        dashboard()
    else:
        print("Invalid USSD code. Try Again!")
        USSD() # recursive function
        
    

def dashboard():
    print("""
    1. Buy Data
    2. Check balance
    #. Exit      
          
    """)


# USSD()


# Types of function: parametized and non-parametized function


def area_of_circle(r, pi):
    aoc = pi * (r**2)
    print(f"AOC: {aoc}cm^2")
    
# area_of_circle(5, 3.142)
# area_of_circle(pi=3.142, r=5)

def area_of_circle(r, pi=3.142):
    aoc = pi * (r**2)
    print(f"AOC: {aoc}cm^2")
    
# area_of_circle(5, 5)


# return function

def get5():
    return 5

# val = get5()
# print(val)


def getAcronym(fullname):
    split = fullname.split()
    if len(split) >= 2:
        first = split[0][0]
        second = split[1][0]
        return first+second
    
    elif len(split) == 1:
        return split[0][0]
    
    else:
        return ""


# fullname = input("Fullname: ").strip().title()
# val = getAcronym(fullname)
# print(val)


# global and local variable

balance = 0
database = []

def dashboard():
    print("""
        1. Deposit
        2. Withdraw
        3. Check Balance
        #. exit
          
    """)
    choice = input("Choice: ")
    if choice == "1":
        deposit()
        
    elif choice == "2":
        withdraw()
        
    elif choice == "3":
        check_balance()
        
    elif choice == "#":
        exit("Goodbye!")
        
    else:
        print("Invalid")
        dashboard()   

def deposit():
    global balance
    
    amount = float(input("Amount: "))
    balance += amount
    
    print("Deposit succesfull")  
    dashboard() 
    
    
def withdraw():
    global balance
    
    amount = float(input("Amount: "))
    balance -= amount
    
    print("Withdrawal succesfull")  
    dashboard() 
    
def check_balance():
    print(f"Your balance is ${balance}")
    dashboard()
    
    
# dashboard()
        
# Anonymous function

hello = lambda: "hello"
# print(hello())


get10 = lambda: 10
# print(get10())

add =  lambda x, y: x+y 
# print(add(5, 6))



# OOP - Object Oriented Programming
# Object :- Is anything that has a property/properties/attributes and can perform a function
# Procedural Oriented programming 
# Benefit OOP:
# 1. More neater code 
# 2. Reusable code 
# 3. Modularization

# class - class is a blueprint/model of the object, hence object can be said to be the instance of a class

# name = "Damilare"
# name2 = "Bash"
# num = 56
# print(type(name))


# class Human:
#     pass


# ada = Human()
# lola = Human()
# print(ada == lola)


class Car:
    brand = "Toyota"
    model = "Land Cruiser"
    
    def drive(self):
        print(f"The {self.brand} {self.model} is Driving...")
        
    def park(self):
        print("parking...")
    
    
car1 = Car()
car2 = Car()

# car1.model = "Corolla"
# print(car2.model)

# car1.park()
# car1.drive()


class Calculator:
    name = 'Porpo Calculator'

    def home(self):
        print(self.name, "\n")
        
        self.value1 = float(input("Value 1: "))
        self.value2 = float(input("Value 2: "))
        
        print("""
        1. Addition
        2. Subtraction
        #. Exit      
              
        """)
        choice = input("Choice: ")
        if choice == "1":
            print(f"Ans: {self.value1 + self.value2}")
            self.proceed()
            
        elif choice == "2":
            print(f"Ans: {self.value1 - self.value2}")
            self.proceed()
        elif choice == "#":
            exit("Goodbye!")
        else:
            print("Invalid 1")
            self.proceed()
            
    
    def proceed(self):
        action = input("Press enter to repeat or # to exit: ")
        if action == "#":
            exit("Goodbye!")
        self.home()
            
calc = Calculator()
calc.home()
     

# Modularization
# SQL - DBMS
# File handling
# Error handling
# Regular expression
# Ipython
# Git/Github
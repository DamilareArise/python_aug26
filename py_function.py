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
    
    
dashboard()
        
#Anonymous function
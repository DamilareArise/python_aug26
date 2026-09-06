# DBMS - Database management system is a system that help manage a digital database ( a place where data are stored, retrieve or managed. )

# Types of DBMS
# 1. RDBMS - (Relational DBMS) / SQL - Structured Query Language
# i. data are in tabular form 
# ii. the tables are relatable using key
# e.g MySQL, PostgreSQL, Oracle, SQLLITE, MSSQL, MariaDB

# 1. create a database
# 2. create a table (rows and column)

# relationships between tables in SQL


# 2. NON-RDBMS / NoSQL
# 1. data are in key-value pair, documents or tree like structure
# e.g MongoDB, redis, firebase




# scripts -  is a file with executable code
# module - is a scripts that contains variables, or functions or classes
# library - is a collection of two or more modules
# framework - use to streamline workflow in a domain e.g django, keras, scikit , bootstrap, laravel, angular



import time, random

# print("loading....")
# time.sleep(3)
# print("done")

# print(random.choice([1, 2, 4, 5]))
# print(random.randint(1000000000, 1099999999))

import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
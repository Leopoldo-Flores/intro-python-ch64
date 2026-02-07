# Python basics - Session #1

print("Hello World from Python") #No semicolon needed
print(2) # printing a number
print(5 + 3) #print results

# ctl + s to save file
# up on arrow key in terminal for previous line

"""
This is a multi-line comment (docsting)
Triple quotes let you write longer explinations.
"""

# --- VARIABLES AND CONATENATION ---
name = "Leo"
age = 23
print(name, age) # Prints variable
print("My name is " + name + " and i am " + str(age) + " years old.")

# -- F-String (modern concatenation)
middle_name = "javier"
last_name = "flores"
# Naming conventions snake_case
print(f"hello")
print(f"My name is {name} {middle_name} {last_name} and i am {age} years old.")
# tab key fills out variable

# Multi-line f-string
print(f"""
My name is {name} {middle_name} {last_name} 
and i am {age} 
years old.
""")

# MINICHALLENGE 1
"""
- Create 4 variables: my_name, my_last_name, my_age, and my_favorite_technology.
- Assign them your own information or mockdata.
- Then, use an f-string to print a scentence like in the previous example
"""

# ---TYPE FUNCTION---
print(type(name)) # <class 'str'>
print(type(age))  # <class 'int'>
print(type(True)) # <class 'bool'>
# highlight and crtl + / creates comment

# -- Casting (Changing Data Types) ---
print(20 + int("20"))  # 40
print(20 + age)        # 43
print(20 + 2.98)       #22.98

# --- INPUT FUNCTION ---
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# print(type(input("Enter your age:")))

# user_age = int(input("Enter your age: "))
# print(age + user_age)
# print(f"you are {user_age} years old")

# --- Mini Challenge 2 ---
"""
Pizza Calculator
    - Ask how many slices of pizza and how many people.
    - Use math operatos to calculate slices per person.
    - Show the result with an f-string.
"""


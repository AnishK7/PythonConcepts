"""
EAFP: Asking for Forgiveness, Not Permission
"""
# Also Duct Typing


# Example 1

class Duck:

    def quack(self):
        print("Quack Quack")

    def fly(self):
        print("Flap Flap")




class Person:

    def quack(self):
        print("I am quacking like a duck")

    def fly(self):
        print("I am flapping like a duck")


def quack_and_fly(thing):
    # Non Duct typing and Non Pythonic
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print("This has to be a duck")


    # Look Before you Leap(LBYL) Non Pythonic way too
    # if hasattr(thing, 'quack'):  # Asking for Permission
    #     if callable(thing.quack): # Asking for Permission
    #         thing.quack()
    
    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()


    # EAFP
    try:
        thing.quack() # First trying rather than checking/Asking for permission
        thing.fly()
        thing.bark() # This would ask for forgiveness as therre is no bark method available
    except AttributeError as e: # Asking forgiveness in case of exception
        print(e)
    

d = Duck()
p = Person()


#quack_and_fly(d)
#quack_and_fly(p)


# Example 2

#person = {'name':'AJ', 'age':23, 'gender':'M', 'job':'Developer'}
person = {'name':'AJ', 'age':23, 'gender':'M'}


#LBYL (Non Pythonic)

# if 'name' in person and 'age' in person and 'gender' in person and 'job' in person:
#     print("I'm {name}, {gender}, {age} years old and a {job}".format(**person))
# else:
#     print("Missing some keys")


# #EAFP (Pythonic)

# try:
#     print("I'm {name}, {gender}, {age} years old and a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} key".format(e))


# Race Condition

import os


my_file = 'boom.txt'

# Non Pytonic
if os.access(my_file, os.R_OK): #Suppose if the condition passes here
    with open(my_file) as f:     # Bt by the time it reaches here, the access is changed, then it would print file is not accessable but printing that after going inside the if block which becomes harer to debug
        print(f.read())

else:
    print("File has no access")


#Pythonic way
try:
    f = open(my_file)
except IOError as e:
    print("File cannot be accessed")
else:
    with f:
        print(f.read())

from functools import wraps

"""
Decorators
"""

# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before')
#         return original_function()
#     return wrapper_function


# @decorator_function
# def display():
#     print('Display function running')

# When not using the '@'
#display = decorator_function(display)
#display()

# When usig the @
#display()



"""
Using arguments in functions
"""


# def decorator_function(original_function):

#     @wraps(original_function)
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before')
#         return original_function(*args, **kwargs)
#     return wrapper_function


# @decorator_function
# def display():
#     print('Display function running')


# @decorator_function
# def displayInfo(name=None, age=None):
#     print('Name is {} and age is {}'.format(name, age))


# displayInfo('Arjun', 23)


"""
Using Arguments in decorators
"""

def prefix_decorator(prefix):
    def decorator_function(original_function):

        #@wraps(original_function)
        def wrapper_function(*args, **kwargs):
            print('Prefix: '+prefix+' wrapper executed this before')
            return original_function(*args, **kwargs)

        return wrapper_function

    return decorator_function

@prefix_decorator('Boom')
def display():
    print('Display function running')


#@prefix_decorator('Boom with args')
def displayInfo(name=None, age=None):
    print('Name is {} and age is {}'.format(name, age))

#displayInfo('Arjun', 23)
#display()

# Or

displayInfo = prefix_decorator('Boom with args')(displayInfo)
displayInfo('Arjun', 23)
# Here prefix_decorator('Boom with args') becomes a function that accepts an argument: displayInfo which returns a function that accepts arguments *args, **kwargs

# Hence we can do this also:
#displayInfo = prefix_decorator('Boom with args')(displayInfo)('Arjun', 23)
#displayInfo


"""
Decorator Class
"""

# class decorator_class(object):

#     def __init__(self, function):
#         self.function = function


#     def __call__(self, *args, **kwargs):
#         print('Call method of class 1 executed')
#         return self.function(*args, **kwargs)
    
    

# class decorator_class_2(object):

#     def __init__(self, function):
#         self.function = function


#     def __call__(self, *args, **kwargs):
#         print('Call method of class 2 executed')
#         return self.function(*args, **kwargs)
  
    
# @decorator_class
# def displayInfo(name=None, age=None):
#     print('Name is {} and age is {}'.format(name, age))



# #@decorator_class_2
# #@decorator_class
# def display():
#     print('Display function running')


# #displayInfo('Arjun', 23)


# #display()

# # OR

# #display = decorator_class_2(decorator_class(display))
# #display()

# # Simplifying it:

# display = decorator_class(display)
# display = decorator_class_2(display)
# display()

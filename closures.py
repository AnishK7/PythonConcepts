# First class function or Higher order function or closures- treat a function as a variable, pass function as an argument, return a function from the function



# def square(x):
#     return x*x

# #f = square # First class function
# #print(f(5))


# def myMap(func, arg_list): # Higher order function
#     result = []
#     for arg in arg_list:
#         result.append(func(arg))
#     return result

# squares = myMap(square, [1,2,3,4,5])
# print('squares', squares)


# Higher Order fn: returning a function

# def logger(msg):

#     def logMessage():
#         print('Log:', msg) # Here msg is a free variable as it has its scope to outer fn as well as inner fn
        
#     return logMessage




# log_hi = logger('Hi!')
# log_hi()

# Closure: A function which has access to the parameters passes to the local scope when th closure was created

# def html_tag(tag):

#     def wrap_text(msg):
#         print('<{0}>{1}</{0}>'.format(tag, msg))

#     return wrap_text

# print_h1 = html_tag('h1')
# print_h1('Boom')
# print_h1('Another Boom')

# print_p = html_tag('p')
# print_p('Paragraph')





# Calling fn from fn


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def OutsideFn(funcName):
    def insideFn(*args):
        print("Calling {0} function with arguments {1} and the result is : {2} ".format(funcName.__name__, args, funcName(*args)))


    def insideAnotherFn():
        def insideAnotherFnLevel2(*args):
            print("Calling {0} function with arguments {1} and the result is : {2} ".format(funcName.__name__, args, funcName(*args)))

        return insideAnotherFnLevel2

        
    #return insideFn
    return insideAnotherFn


    

#boom = OutsideFn(add)
#boom(3,3)
#boom = OutsideFn(sub)
#boom(3,3)


boom = OutsideFn(add)
boom = boom()
boom(3,3)
















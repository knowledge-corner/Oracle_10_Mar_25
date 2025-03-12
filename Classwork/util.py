# Assumption - This is a util library and contains functions for numeric calculations

print("Start of util module")

def is_int(func):  # func is the function object and the function with the decorater is passed to func variable
    print("Inside is_int")
    def check(param) : # param takes the parameters passed to the calling function
        print("Inside check")
        if type(param) == int :
            print("Inside check - if condition is true")
            return func(param)
        else:
            print("Inside check - if condition is false")
            return "Error in the parameter"
    return check

@is_int
def factorial(num) :
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact

def is_even(num) :
    return num % 2 == 0

def is_prime(num):
    for i in range(2, num) :
        if num % i == 0 :
            return False
    else:
        return True

def add(num1, num2) :
    return num1 + num2
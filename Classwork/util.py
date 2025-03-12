# Assumption - This is a util library and contains functions for numeric calculations

def is_int(func):  # func is the function object and the function with the decorater is passed to func variable
    def check(*param) : # param takes the parameters passed to the calling function      
        # Check if all the values in the param tuple are int or not       
        if all(map(lambda num : type(num) == int, param)) :           
            return func(*param)
        else:
            return "Error in the parameter"
    return check

@is_int
def factorial(num) :
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact

@is_int
def is_even(num) :
    return num % 2 == 0

@is_int
def is_prime(num):
    for i in range(2, num) :
        if num % i == 0 :
            return False
    else:
        return True

@is_int
def add(num1, num2) :
    return num1 + num2


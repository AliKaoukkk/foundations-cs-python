def factorial(n):
    if n == 0:
        return 1
    elif n < 0 :
        print('please enter a positive value')
    else:
        return n * factorial(n - 1)
n = eval(input('enter a number'))
print("The factorial of " + str(n)  + ' is' , factorial(n) )
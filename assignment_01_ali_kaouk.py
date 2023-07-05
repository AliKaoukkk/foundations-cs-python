#Question 1:

def factorial(n):
    if n == 0:
        return 1
    elif n < 0 :
        print('please enter a positive value')
    else:
        return n * factorial(n - 1)
n = eval(input('enter a number'))
print("The factorial of " + str(n)  + ' is' , factorial(n) )
print('-----------------------------------------------------')
#Question 2:

def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


num = int(input("Enter an integer: "))
result = find_divisors(num)
print("Divisors:", result)
print('------------------------------------------------------')
#Question 3:

def reverseString(string):
    reversed_string = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string
user_input = input("Enter a string: ")
reversed_input = reverseString(user_input)
print("Reversed string:", reversed_input)
print('---------------------------------------------')
#Question 5:

import re

def stringPassword(password):
    if len(password) < 8:
        return False
    elif not re.search('[A-Z]', password):
        return False
    elif not re.search('[a-z]', password):
        return False
    elif not re.search('\d', password):
        return False
    elif not re.search('[$#?@!]', password):
        return False
    else:
      return True
password = input("Enter a password: ")
if stringPassword(password):
    print("Strong password")
else:
    print("Weak password")
#Question 4:

def evenNumbers(input_list):
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
user_input = input('whats your number')
user_list = list(map(int, user_input.split()))
result = evenNumbers(user_list)
print(result)

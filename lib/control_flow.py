#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
   

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

# Test cases
print(hows_the_weather(30))  # "It's brisk out there!"
print(hows_the_weather(50))  # "It's a little chilly out there!"
print(hows_the_weather(90))  # "It's too dang hot out there!"
print(hows_the_weather(70))  # "It's perfect out there!"



def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

# Test cases
print(calculator('+', 3, 4))  # 7
print(calculator('-', 10, 5)) # 5
print(calculator('*', 6, 7))  # 42
print(calculator('/', 8, 2))  # 4.0
print(calculator('%', 9, 3))  # Invalid operation!, None

  

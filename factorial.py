print("Program to calculate Factorial of any number")

number = int(input('Enter the number (must be equal and greater than 0)\t'))  #Type casting string to int.


def factorial(number):

    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return (factorial(number - 1)) * number 

print(f'The result of {number}! is',factorial(number))


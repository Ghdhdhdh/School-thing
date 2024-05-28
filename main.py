#!/usr/bin/env python3


# Needs the following:
# assignment Variable/Class
# Class
# Statment/Keyword
# Try Catch
# Function Declaration
# Function Call
# int, str, float and None
# List
# For
class +():

valid_opperands = ['+', '-', '*', '/', 'Q', 'q']
import sys
print('Command Line Calculator')
print("\n")
ans = None

def Terminalinput():
    #brings in terminal input for a starting number
    print('Enter a number')
    while True:
        if ans != None:
            print('Use _ to use the last result')
        x = input()
        if x == '_' and ans != None:
            return ans
            break
        elif x == '_' and ans == None:
            pass
        return x

def get_symbol():
    #function to recieve user input for surroundings
    while True:
        print('\n')
        print('Determine how you want to process the two numbers')
        print('Enter + for addition')
        print('Enter - for subtraction')
        print('Enter * for multiplication')
        print('Enter / for division')
        print('Enter Q to exit the calculator')
        print("Enter ^ for powers")
        x = input()
        if x in valid_opperands:
            return x
        elif x == 'Q' or x == 'q':
            sys.exit()
        else:
            print("Invalid Input")

def calculate(symbols, num1s, num2s):

    for symbol in valid_opperands:
        while True:
            try:
                return num1s ** num2s
                break
            except TypeError:
                pass

while True:
    num1 = Terminalinput()
    symbol = get_symbol()
    num2 = Terminalinput()

    ans = calculate(str(symbol), int(num1), int(num2))

    print(f"The answer is {ans}")


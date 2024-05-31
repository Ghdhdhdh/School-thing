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
import sys
class plus():
    def __init__(self):
        pass
        self.toprint = """
        To use addition, press the + key and then press enter
        """
        self.total = 0
    def oper(self, num1, num2):
        self.total = self.total + (num1 + num2)
        pass
        return num1 + num2
    def print(self):
        return self.toprint
class multiply():
    def __init__(self):
        pass
        self.toprint = """
        To use multiplication, press the * key and then press enter
        """
        self.total = 0
    def oper(self, num1, num2):
        self.total = self.total + (num1 * num2)
        return num1 * num2
    def print(self):
        return self.toprint    
class subtract():
    def __init__(self):
        pass
        self.toprint = """
        To use subtraction, press the - key and then press enter
        """
        self.total = 0
    def oper(self, num1, num2):
        self.total = self.total + (num1 - num2)
        return num1 - num2
    def print(self):
        return self.toprint
class divide():
    def __init__(self):
        pass
        self.toprint = """
        To use divisoion, press the - key and then press enter.
        """
        self.total = 0
    def oper(self, num1, num2):
        self.total = self.total + (num1 / num2)
        return num1 / num2
    def print(self):
        return self.toprint
class quit():
    def __init__(self):
        pass
        self.toprint = """
        to quit, press the q key and then press enter
        """
    def quit(self):
        sys.exit()
    def print(self):
        return self.toprint
add_class = plus()
multiply_class = multiply()
subtract_class = subtract()
divide_class = divide()
quit_class  = quit()
valid_opperands = {'+':add_class, '-':subtract_class, '*':multiply_class, '/': divide_class, 'Q': quit_class, 'q': quit_class}
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
        
        
        for key, value in valid_opperands.items():
            print(value.print())
        x = input("Input the symbol: ")
        for key, value in valid_opperands.items():
            if x == key:
                return value
            else:
                print("You entered an incorrect value. Try again.")
            

def calculate(symbol, num1s, num2s):

    return symbol.oper(num1s, num2s)

while True:
    num1 = Terminalinput()
    symbol = get_symbol()
    num2 = Terminalinput()

    ans = calculate(symbol, int(num1), int(num2))

    print(f"The answer is {ans}")


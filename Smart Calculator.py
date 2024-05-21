import random
import math
import os

t = 2
l = 0
tp = 0
print("welcome to the Smart Calculator.")
print("Type your first number to get started. You have " + str(t) + " tokens, and each token is worth 1 question. Type \"e\" at any time to forfeit the rest of your tokeins and end the session.")
for i in range(t):
    a1 = i + 1
    a = t - a1
    numOne = str(input("Put in your first number.\n"))
    if numOne == "e":
        while True:
            exit()
    op = str(input("Put in your function. Multiplication is *, exponentation is ** divisionn is /, addition is +, subtraction is -, square root is sqrt, factorial is !.\n"))
    if op == "*":
        print("This is multiplication. It is repeated addition.")
        numTwo = int(input("Put in your second number.\n"))
        ans = int(numOne) * numTwo
    elif op == "**":
        print("This is exponentation. It is repeated multiplecation.\n")
        numTwo = int(input("Put in your second number.\n"))
        ans = int(numOne) ** numTwo
    elif op == "/":
        print("This is division. It is repeted subtraction. You cannot divide by zero.")
        numTwo = int(input("Put in your second number.\n"))
        ans = int(numOne) / numTwo
    elif op == "+":
        print("This is addition. It is combining two numbers together.")
        numTwo = int(input("Put in your second number.\n"))
        ans = int(numOne) + numTwo
    elif op == "-":
        print("This is subtraction. It is taking a certain amount and removing that amount from the original number.")
        numTwo = int(input("Put in your second number.\n"))
        ans = int(numOne) - numTwo
    elif op == "sqrt":
        print("This is square root. It is taking a number, and seeing what times itself equals that number.")
        ans =  math.sqrt(int(numOne))
    elif op == "!":
        print("This is factorial. It is taking a number, adding one to it and multipling them together, starting at one. for example, 4! is 1*2*3*4, which equals 24.")
        ans = math.factorial(int(numOne))
    elif op == "e":
        while True:
            exit()
    if a == 1:
        tp = " token "
    elif a > 1:
        tp = " tokens "
    else:
        tp = " tokens "
    print("Your answer is " + str(ans) + ".")
    print("You have " + str(a) + str(tp) + "left.")
input("You have used all your tokens. Press enter.\n")
while True:
    exit()

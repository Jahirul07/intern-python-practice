# Python program to divide two numbers using function

from __future__ import division


def div_Num(num1, num2): #user-define functionurn 
    div = (num1 / num2) #divide numbers
    return div #return value

#take inputs
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# function call

division = div_Num(num1, num2);

#print value

print("The divition of {0} and {1} is {2}".format(num1,num2,division));



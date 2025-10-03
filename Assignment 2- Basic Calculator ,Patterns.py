"""Task 1: Create a basic calculator program that can perform various arithmetical operations. 
Implement control structures to handle user input and perform the desired operation using appropriate operators. 
In this assignment, you will create a simple calculator program using Python. 
The program will prompt the user to enter two numbers and select an operation
 (addition, subtraction, multiplication, modulo, exponentiation, floor division and division). 
 Based on the user's choice, the program will perform the corresponding operation using 
 control structures such as if-elif-else statements. 
 Operators such as +, -,*,%,**,// and / will be used to perform calculations. 
 
 Task 2 : Students need to write a Python program that generates a numeric pattern based on the given structure. 
 The pattern consists of rows of numbers, where each row starts from the row number and decrements to 1. 
 The pattern demonstrates a clear use of nested loops and logical control structures in Python.
"""

#Task 1 --- Calculator

result=0
print("             A Simple Calculator")
print("---------------------------------------------------------")
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))

print("Select an option from the given (Enter only the option number):")
print("1.Addition           2.Subtraction       3.Multiplication    4.Division")
print("5.Exponentiation     6.Floor Division    7.Modulo")

option=int(input("Enter an option"))

if option==1:
    result=num1+num2
    print("The sum of the given two numbers are : ",result)
elif option==2:
    result=num1-num2
    print("The Difference of the given numbers are : ",result)    
elif option==3:
    result=num1*num2
    print("The Product of the given numbers are : ",result) 
elif option==4:
    result=num1/num2
    print("The Divided result of the given numbers are : ",result) 
elif option==5:
    result=num1**num2
    print("The Exponential result of the given numbers are : ",result) 
elif option==6:
    result=num1//num2
    print("The Floor Division Result of the given numbers are : ",result)    
elif option==7:
    result=num1%num2
    print("The Modulus of the given numbers are : ",result)    
else:
    print("I Think You didn't followed the instructions properly ^_^  ")


#Task 2 --- 

print("         A Simple pyramid of numbers : ")
print("---------------------------------------------------------")
for i in range(1,6):            # 6 is used because when i gave 5 ,it only prints upto 4
    for j in range(i,0,-1):      
        print(j,end=" ")
    print()  

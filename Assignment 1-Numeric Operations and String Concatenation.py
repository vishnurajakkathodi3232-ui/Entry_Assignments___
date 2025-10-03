# Assignment 1: Numeric Operations and String Concatenation

# Write a Python program that performs basic numeric operations and string concatenation. 
# Create a program that: - Accepts two numeric inputs from the user.
# Performs addition, subtraction, multiplication and division operations on the numeric inputs. 
# Concatenates the two inputs as strings and prints the result

# -----------------------------------------------------------------------------------------------------------

number1=int(input("Enter the first number : "))
number2=int(input("Enter the second number : "))

sum=number1+number2
print("The Sum of the given Two Numbers are : ", sum)

diff=number1-number2
print("The Difference of the given two numbers are : ", diff)

mul=number1*number2
print("The Product of the given two numbers are : " , mul)

div=number1/number2
print("The Divided Result of the given numbers are : ", div)


#---------------------------------------------------------------------------------------------------------------

str1=input("Enter the first String : ")
str2=input("Enter the second String : ")

concat=str1 +" "+ str2
print("The Concatenated String is : ",concat)

#-------------------------------------------------------------------------------------------------------------------
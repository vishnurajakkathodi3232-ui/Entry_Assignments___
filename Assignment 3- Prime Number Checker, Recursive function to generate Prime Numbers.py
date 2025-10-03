#Task 1:-

"""Task 1: Create a Python module that checks whether a given number is prime or not. 
Implement this functionality using a user-defined function for checking primality and 
utilizing the math module for mathematical operations. 
You need write a module named my_prime(n) that takes an integer n as input and returns True if 
n is a prime number, and False otherwise. 
Utilize the math.sqrt() function from the math module to optimize the primality checking process. 
Use the user-defined prime module in your program to check whether the entered number is prime or not. 
Run the program twice and check whether the output is received as expected 
Sample Input: Case 1 Input Number: 17 Expected Output: True 
Sample Input: Case 2 Input Number: 20 Expected Output: False """

"""
print("     PROGRAM TO CHECK A NUMBER IS PRIME OR NOT   \n")
import math

def my_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n=int(input("Enter a number\n"))
print(f"Input Number: {n}")
print("Expected Output:", my_prime(n))
"""



#Task 2:-

"""
Task 2:-Students need to write a Python program that generates and prints all prime numbers 
within a given range using recursion. The program should take two positive integers as input 
(start and end of the range) and use recursive logic to determine and print the prime numbers in that range. 
Write a Python program to print all prime numbers in a given range using recursion. 
A prime number is a number greater than 1 that has no divisors other than 1 and itself. 
The program should use a recursive function to check for primality and another function
 to iterate through the range recursively. Input: Two positive integers: start and end, 
 where start is the beginning of the range and end is the end of the range (inclusive). 
 Output: A list of all prime numbers in the given range. If no prime numbers exist in the range, 
 print an empty list. Example: Input: start = 0, end = 10 Output: [2, 3, 5, 7]
"""

"""
print("Recursive function to find all primes in the range [start, end]")
print("--------------------------------------------------------------------")
def is_prime(n, i=2):

    if n <= 1:
        return False
    if i > int(n ** 0.5):  
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

def find_primes(start, end):
    
    if start > end:
        return []
    if is_prime(start):
        return [start] + find_primes(start + 1, end)
    else:
        return find_primes(start + 1, end)

start=int(input("Enter the starting range :  "))
end=int(input("Enter the ending range :  "))

prime_list = find_primes(start, end)
print("Prime numbers between", start, "and", end, ":", prime_list)
"""
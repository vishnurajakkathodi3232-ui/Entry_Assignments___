#Assignment 5: Performance Monitoring for Data Streaming and Python Text Data Analysis Program

"""
Task 1:-Implement a generator function that simulates data streaming, yielding random numbers between 1 and 100. 
Use a decorator to enhance this generator by adding a feature that logs the time taken to iterate through the entire generator.
 You have to demonstrate how decorators can add functionality to generators without modifying the generator's code. 
 This assignment simulates a common scenario in data processing where both data streaming and performance monitoring are essential.
  Generator Function: Simulate a data stream by yielding random numbers.
    Decorator Function: Measure the execution time of iterating through the generator. 
""" 

import time
import random

# Decorator Function

def numbers_stream(generator_func):
    def wrapper(*args, **kwargs):
        start = time.time()         # start time is used to record starting time

        gen = generator_func(*args, **kwargs)

        results = []
        for value in gen:
            results.append(value)

        end = time.time()           # end time is used to record the ending time
        print(f"Time taken: {end - start:.6f} seconds") # .6f is used to return seconds upto 6 decimal places

        return results   # generated values will be displayed
    return wrapper

# Generator Function

@numbers_stream   # decorator function is used
def data_stream(n):
    
    for i in range(n):
        yield random.randint(1, 100)

# Main Program

if __name__ == "__main__":
    numbers = data_stream(10)           # just gave 10, we can give how much we want(more then 100 also possible )
    print("Generated Numbers:", numbers)
    print("---------------------------------------------------------------------------------------")







"""    
    Task 2:-You are tasked with creating a Python program that utilizes regular expressions to process and analyze text data.
    Your program should perform the following tasks: -Extract all email addresses from a given text.
      -Identify and extract all phone numbers in a specified format. -Replace all occurrences of a particular word with another word. 
      Regular expressions are powerful tools for pattern matching and searching within text data.
        In this assignment, you will familiarize yourself with basic regular expression syntax and 
        learn how to apply it to solve common text processing tasks.

"""

import re

# -----------------------------
# Sample text data
# -----------------------------
text = """
Hello, my name is VISHNURAJ A. 
You can contact me at vishnu123@gmail.com or vishnu456$gmail.com        
My phone numbers are 987-654-3210 and 98657-43522.                  # one number doesn't match the format, it wont be accepted
I love Python Programming . Python Programming is interesting.
"""
# in the above text one email and one phone number doesn't match the required formats, it wont be accepted



# Extract all email addresses

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)    # to specify the format and characters
print("Email Addresses Found:", emails)

# 2. Extract all phone numbers (format: 12345-67890)

phones = re.findall(r"\d{5}-\d{5}", text)               # to specify the format of mobile number
print("Phone Numbers Found:", phones)

# 3. Replace a word with another word

replaced_text = re.sub(r"Programming", "Development", text)
print("\nText after replacement : \n")
print(replaced_text)



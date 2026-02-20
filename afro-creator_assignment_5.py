"""
COMP 163 - Introduction to Programming
Assignment: Chapter 5 - Loop Mastery
Name: Hakeem Cole
GitHub Username: afro-creator745
Date: 2/20/2026
Description: A series of different methods of using for and while loops to fix given problems.
AI Usage: AI was used for step 3 to find how to properly align the numbers for the table
in particular it taught me how to add spaces inbetween values using f"{row:2}"
which makes sure that the value row will atleast take up 2 spaces
"""

"""
I wanted to comment that deiciding whether to use for loops or while loops is fairly simple because
if I'm dealing with a set number of values or list I would use a for loop. Otherwise I'll use a while loop
"""
#Collatz Conjecture Sequence
current_num = int(input("Enter starting number: "))   # Log in input
steps = 0            #creating necessary variables and lists
sequence_list = []

while current_num > 0:  # only repeats in the integer input is positive
    current_num=int(current_num)         # converts floats to integers before it's added to the list to match the display on the doc.
    sequence_list.append(current_num) #Tracks the sequence of numbers, adding them to a list
    if current_num == 1:  # This is here so the value 1 can still be added to the list but still end the loop
        break
    if current_num % 2 == 0: #Checks if number is even then proceeds to run through the rules for even numbers
        current_num /= 2
    elif current_num % 2 != 0 and current_num != 1: #Checks if number is odd then proceeds to run through the rules for odd numbers
        current_num *= 3
        current_num += 1
    steps += 1  #Counts how many times the loop repeats

print("Sequence:", end=' ')
for current_num in sequence_list:    #line 20-22 prints every value collected in the sequence list
    print(current_num, end=' ')
print('\nSteps:', steps)  #prints the step count on a new line


#Prime Number Checker
current_num = int(input("\nEnter a number: "))
print('Testing divisors from 2 to', str(current_num-1) + "...") #prints the range of divisors it's using
for number in range(2, current_num):       #Dividing from 2 to one least than the input number
    prime_checker = current_num % number
    if prime_checker == 0:    #once a divisor is found it'll output this statement and end the for loop
        print(current_num, "is not prime (divisible by", str(number)+ ')')
        break
else :
    print(current_num, "is a prime!") # if it goes through all number without the if-statement being true the number will print prime


#Multiplication Table Grid
print("\nMultiplication Table:")
print("   ", end='')
for header_row in range(1, 11):  #prints out the header row for the table
   print(f"{header_row:2}", end=" ")
print()
for row in range(1, 11): #starts the row printing
    print(f"{row:2}", end=" ")
    for col in range(1, 11): # prints the value of the table
        print(f"{row * col:2}", end=" ")
    print() # move to the next row

#Integration Challenge - Statistics Dashboard
print("\n=== Statistics Dashboard ===")
print("Enter positive numbers (enter -1 to finish):")     # prints the  starting headings to match the output
user_num = int(input("Enter a number: "))
num_count = 0           # setting needed variables and list
sum = 0
number_list = []
while user_num > -1:    #Continues to take inputs from the user until false
    number_list.append(user_num)
    num_count += 1                   #Adds number inputs to a list and counts the amount of inputs
    user_num = int(input("Enter number: "))
for number in number_list:           #finds the sum using for loops and list
    sum = number + sum

min_num = number_list[0]      #setting a minium value for the for loop, for loop checks for a smaller value
for number in number_list:
    if number < min_num:
        min_num = number

max_num = number_list[0]  #setting a max value, for loop checks for a higher value
for number in number_list:
    if number > max_num:
        max_num = number

#printing out all the colllected data in the proper format
print('\n=== Statistics ===')
print("Count:", num_count, 'numbers')
print("Sum:", sum)
print("Average:", f"{sum/num_count:.1f}")
print("Minimum:", min_num)
print("Maximum:", max_num)

#Uses a for loop to print the bar chart properly
print("\n=== Bar Chart ===")
for number in number_list:
    print(f"{number:2}:","*" * number)

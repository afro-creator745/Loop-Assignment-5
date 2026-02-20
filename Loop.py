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
print('Testing divisors from 2 to', str(current_num-1) + "...")
for number in range(2, current_num):
    prime_checker = current_num % number
    if prime_checker == 0:
        print(current_num, "is not prime (divisible by", str(number)+ ')')
        break
else :
    print(current_num, "is a prime!")


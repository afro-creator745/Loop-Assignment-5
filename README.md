[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IiqXY2S6)
# Loop Mastery Assignment

**Student Name:** Hakeem Cole  
**GitHub Username:** afro-creator745  
**Date:** 2/20/2026

## Overview

This assignment demonstrates mastery of while loops, for loops, and nested loops through four programming challenges. Each challenge was selected to showcase the appropriate loop type for different problem scenarios.

---

## Loop Type Analysis

### Step 1: Collatz Sequence - While Loop

**Why while loop?**  
A while loop is best here because you can't know how many iterations you need for every input. Thus the while loop will continue until the condition of the number being equal to 1 and then the loop will end.

**How it works:**  
My loop condition only check if the number entered is postive. Thus this loop would continue forever if I never added an if statement that checks when the cuurent number equals 1 and then it'll procceed to break the loop. 

**Example:**
```
Enter starting number: 13
Sequence: 13 40 20 10 5 16 8 4 2 1
Steps: 9
```

---

### Step 2: Prime Checker - For Loop

**Why for loop?**  
A for loop works best here since we know how many times we would need the loop to repeat. You know the range is 2 to the input number. 

**How it works:**  
I used % to determine whether the number had a divisor because if the operation returned 0 that means the number has an even divisor. Thus I would have the code end there with a break statment after displaying the proper message.

**Example:**
```
Enter a number: 17
Testing divisors from 2 to 16...
17 is prime!
```

---

### Step 3: Multiplication Table - Nested Loops

**Why nested loops?** 
A nested loop is nned because you need a loop for the rows and another to make the columns. the outer loop would create the next row while the inner loop would add the correct values to their corresoponding positions on the table. 


**Outer vs Inner:**  
THe outer loop handled the row and the inner loop handles the colummns. Whcih makes sence since python displays line by line thus the row must be made and then we fill n the columns. 
**How it works:**  
Using f"{row:2}" ensured that the numbers would take up the same amount of spaces whether it was on digit or 2 digits. 
using f"{col:2}" ensured the same  outcome as f"{row:2}"

**Example:**
```
Multiplication Table:
    1   2   3   4   5   6   7   8   9  10
 1  1   2   3   4   5   6   7   8   9  10
 2  2   4   6   8  10  12  14  16  18  20
...
```

---

### Step 4: Statistics Dashboard - All Three Loop Types

**Why all three?**  
For step 4 I only used for loops and while loops, I didn't need to implment nested loops.
- **While loop:** The while loop was used to get as many inputs the user would like to enter. 
- **For loop:** After collecting the users inputs and adding them to a list, I then knew how many times I need to repeat my loop hence I used a for loop.
- The for loops where used to find the minimum, maximum and sum.
- **Nested loops:** [Wasn't used

**How it works:**  
I collected the majority of my data in the while loop. Under the while loop I'll add the users inputs to a list and collect the count. From there I could've use list functions to get the desired data for the outputs. But instead I used for loops to add all the data up to get the sum. I then used for loops to check for the min and max values by setting the min and max vaules to the first value in the list. Then I used the for loop to comapre every other value to the already set min and max values and if a value was either lower or higher it'll set that value as the new min or max.
To create the bar chart I just had a for loop repeat a print statemnt of each number that was the same as the example oputpuut 
- How you collect data
- How you calculate statistics
- How you create the bar chart

**Example:**
```
=== Statistics Dashboard ===
Enter positive numbers (enter -1 to finish):
Enter number: 5
Enter number: 12
Enter number: 8
Enter number: 15
Enter number: 3
Enter number: -1

=== Statistics ===
Count: 5 numbers
Sum: 43
Average: 8.6
Minimum: 3
Maximum: 15

=== Bar Chart ===
 5: *****
12: ************
 8: ********
15: ***************
 3: ***
```

### Edge Cases Considered

I didn't have any case where I have to test the code. 
- Example: What happens with very large numbers in Collatz?
- Example: How does the prime checker handle 2?
- Example: What if user enters only one number in statistics?

---

## Challenges and Solutions

### Challenge 1: I didn't face to many challenges but I did have an issue where my list would only have one value
**Solution:** The problem was the line of code that defined a blank list was under my loop function so a number would get added to the list but then it'll get removed because the list would get set to blank again. Thus I moves the blank list to outside of the loop and the problem was solve. 

### Challenge 2: I have a problme with fomratting the multiplcation table
**Solution:** I used AI to see what I was mising and hen I procceed to the fix my mistake 



---

## Key Learnings

The most challenging part is the critical thinking and determining how you should appoarch each problem. But other than that the assignment is not that hard but it's definitely keeps the mind sharp. The while loops are pretty similar to C++ but the for loops aee completely different but I like them more and I see the potenital of them.  
- What did you learn about choosing the right loop type?
- What was the most challenging part?
- How did this assignment improve your programming skills?

---

## AI Usage

[Choose one:]


**Option B - AI Used (be specific):**
AI assistance was used for the following:

1. **How to properly format the multiplcation table**  
   - What you asked: I had AI solve the mulitplcation table problem. The I asked for it to explain f"{row:2}"
   - What you learned: I compare code to see what I was missing then I asked AI to explain the use of that code and then I implemented into my code
   - How you used it: I learned what f"{row:2}" does to an ouptut. It ensures that the number of object takes up at least 2 digits and if it doesn't it'll added filler sapce to make sure the format is correct


**All core logic and implementation were developed independently after understanding the concepts.**


## Commit History

This assignment was developed incrementally with meaningful commits:

---

**Declaration:** I certify that this assignment is my own work and I have not copied code from other students or unauthorized sources. Any AI assistance used has been properly documented above.

**Signature:** Hakeem Cole 
**Date:** 2/20/2026

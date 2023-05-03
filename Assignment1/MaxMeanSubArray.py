'''
MaxMeanSubArray.py
Anthony Avelar
Updated 5/2/2023 
(This is my second attempt at solving this leetcode problem)
'''


# QUESTION: Given an array of integers and an integer "k", find the maximum mean of a subarray of size "k"

# ASSUMPTIONS I MADE:
'''
- I assumed that I have a non-empty array
- I assumed that integer "k" is always going to be a positive integer (k > 0)
- I assumed that I am looking for continuous subarrays
'''

# PROBLEM SOLVING STRATEGY USED: Two Pointer Technique (Fixed-Size Sliding Window)
'''
STEP 1
First, I need to find all contiguous subarrays of size 'k' in the given array of integers. 
I can do this by iterating through the array and creating a new subarray of size 'k' by selecting the current element and the next 'k-1' elements.

> In other words: the first step to solve this problem is to find all the continuous subarrays of size 'k' within the hypothetical array. 
It is important to point out that I am making an assumption here — I have chose to look for CONTINUOUS SUBARRAYS.

> How should I tell the computer to find all the continuous subarrays of size 'k'?
Tell the computer to iterate through the hypothetical array
Tell the computer to select the current element, and the 'k-1' elements

STEP 2
Once I have a subarray of size 'k', I can calculate its mean (average) by summing up all the elements in the subarray and dividing by 'k'.

STEP 3
I can store the maximum mean I've seen so far in a variable, and update it whenever I find a new subarray with a higher mean.

STEP 4
Finally, I return the maximum mean I found.
'''


# THIS IS MY PSUEDOCODE
'''
# DECLARE A FUNCTION
> Name the function "find_max_mean"
> Instruct the computer to associate two arguments with the function: (1) first, an array named "arr" and (2) second, a variable named 'k'

# OBTAIN THE LENGTH OF THE ARRAY
> Declare a variable named "n" to hold this length value

# CHECK IF 'k' IS LONGER THAN THE ARRAY
> this will require an if statement

# DECLARE A VARIABLE DEDICATED FOR HOLDING THE MAXIMUM MEAN VALUE
> Name it "max_mean".
> Assign it a value of negativity infinity (in other words, set it to '-inf')

# CREATE A LOOP
    > This will be a FOR LOOP
    > This loop will generate multiple subarrays equal to length 'k'
    > This loop will calculate the average of each of the generated subarrays
    > This loop will compare the averages of each subarray and identify the biggest one out of all of them

    > You will declare four variables in this loop:
        (1) a variable named "subarray" → this variable will hold the generated subarray
        (2) a variable named "subarray_sum" → this variable will hold the total of the elements within the generated subarray
        (3) a variable named "subarray_mean" → this variable will hold the calculated average of the generated subarray
        (4) a variable named "max_mean" → this variable will hold the value of the largest calculated average (it will be overwritten if needed)

# TELL THE COMPUTER TO RETURN THE VALUE OF "max_mean"
'''


# ACTUAL CODE STARTS HERE


def find_max_mean(arr,k):                        # defines a function named 'find_max_mean'
    n = len(arr)                                 # counts the length of the array and stores it in 'n'
    if n < k:                                    # checks if the value of 'k' is larger than the length of the array
        return None                              # if 'k' is larger than the array, returns "None"
    max_mean = float('-inf')                     # initializes 'max_mean' to have the lowest possible value
    for i in range(n-k+1):                       # sets up a for loop to iterate through the array
        subarray = arr[i:i+k]                    # generates a subarray
        subarray_sum = sum(subarray)             # adds up the elements in the generated subarray
        subarray_mean = subarray_sum / k         # calculates the average of generated subarray and stores it in 'subarray_mean'
        max_mean = max(max_mean, subarray_mean)  # compares the average, if average is higher than current value of "max_mean", overwrites it
    return max_mean


arr = [4,5,-3,2,6,1]                             # manually sets the values in the array
k = 2                                            # manually sets the value of 'k'
print(find_max_mean(arr,k))                      # calls the 'find_max_mean' and prints its output on-screen

arr = [4,5,-3,2,6,1]
k = 3
print(find_max_mean(arr,k))

arr = [1,1,1,1,-1,-1,2,-1,-1,6]
k = 3
print(find_max_mean(arr,k))

arr = [1,1,1,1,-1,-1,2,-1,-1,6]
k = 4
print(find_max_mean(arr,k))



# REFLECTION
'''
(1) This is my second attempt at answering this leetcode problem. In my first attempt I struggled mightily because I lacked sufficient coding knowledge and skill.
My major pain point then was not understanding and visualizing what my script was doing line by line.
I had written a program pieced together from snippets of code gather from online tutorials I read. The result? A mess. My first attempt didn't work.

For my second attempt I used a different approach: reverse engineering. I looked at my UCP fellow peers' programs and recreated what they wrote line by line.
I commented on what I thought each line of code did. When confused, I uploaded a snippet of their code to ChatGPT and asked it for clarification.
To avoid plagiarizing, I credited my peers' work below and I explicitly wrote out my problem-solving strategy and pseudocode (instead of just copy-pasting code)

(2) To answer this leetcode problem, I needed to have knowledge of:
    * what an array is (and how to declare one in Python)
    * what a function is (and how to declare one in Python)
    * what the len() function does in Python
    * what an if statement is (and how to use one in Python)
    * what it means to "call a function"
    * what an argument is (with respect to a function)
    * what it means "when a function returns a value"
    * what it means to initialize a variable
    * what the value of "negative infinity" is in Python ('-inf')
    * what a for loop is
    * what the range() function does in Python (and what values you need to pass to it for proper use)

(3) One improvement I could implement later is a prompt to the end-user to type in the values of 'arr' and 'k'. It was bothersome writing out the values myself!
For example, to collect the value of variable 'k' I could've written this line of code:
    int(input("What is the value of k?"))

(4) I am unable to comment on space/time complexity for my program. Why? I do not know enough about the topic to make an analysis yet.
'''


# TIME SPENT
'''
Total estimate: ~4 hours total
~3 hours for researching tutorials & studying other UCP fellows' code
~30 min for writing my algorithm & pseudocode
~30 min for writing code
~10 min for testing my program
'''


# RESOURCES USED
'''
Online tutorials:
(1) https://leetcode.com/problems/maximum-average-subarray-i/description/
(2) https://www.tutorialspoint.com/maximum-average-subarray-i-in-cplusplus
(3) https://www.geeksforgeeks.org/find-maximum-average-subarray-of-k-length/
(4) https://www.youtube.com/watch?v=m-Dqu7csdJk
(5) https://www.youtube.com/watch?v=pEnY7e-5qLw
(6) https://tutorialcup.com/interview/array/find-maximum-average-subarray-of-k-length.htm

My UCP peers (credit were credit is due):
(1) Peter Mora-Stevens
https://github.com/Uber-Career-Prep-2023/Uber-Career-Prep-Homework-Peter-Mora-Stevens/blob/main/Assignment-1/MaxMeanSubArray.py

(2) Christopher Dowdy
https://github.com/Uber-Career-Prep-2023/Uber-Career-Prep-Homework-Christopher_Dowdy/blob/main/Assignment-1/MaxMeanSubArray.py

(3) Liang Xiao
https://github.com/Uber-Career-Prep-2023/Uber-Career-Prep-Homework-Liang-Xiao/blob/main/Assigment-1/MaxMeanSubArray.py

(4) Lina Mei
https://github.com/Uber-Career-Prep-2023/Uber-Career-Prep-Homework-Lina-Mei/blob/main/Assignment-1/MaxMeanSubarray.py
'''

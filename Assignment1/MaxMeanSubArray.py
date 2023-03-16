# QUESTION: Given an array of integers and an integer "k", find the maximum mean of a subarray of size "k"

# PROBLEM SOLVING STRATEGY USED: Two Pointer Technique (Fixed-size Sliding Window)

# TIME COMPLEXITY: ???

# SPACE COMPLEXITY: ???

# TIME SPENT: +40 minutes

# PSUEDOCODE
# (1) calculate the sum of the first k elements
# (2) iterate the array (do this by adding one element from the right and removing another element from the left) — this is "the sliding window of k length"
# (3) update the max sum of k elements with the larger sum
# (4) calculate the max mean k elements using max sum (the formula will be: max sum / k)


# ASSUMPTIONS MADE
# I assumed that I have a non-empty array
# I assumed that integer "k" is a positive integer (k > 0)


# ACTUAL CODE

def findMaxAverage(arr, n, k):
    # Check if 'k' is positive integer
    if (k > n):
        return -1
    
    # Compute sum of first 'k' elements
    sum = arr[0]
    
    # Creates a loop to iterate
    for i in range (1, k):
        sum += arr[i]
        
    max_sum = sum
    max_end = k-1
    
    # Compute sum of remaining subarrays
    for i in range (k, n):
        sum = sum + arr[i] - arr[i - k]
        
        if (sum > max_sum)
            max_sum = sum
            max_end = 1
    
    # return starting index
    return max_end - k + 1


# REFLECTION
# (1) I struggled with this one. I spent the majority of my allotted 40 minutes googling the basic concepts, since I'm still a beginner to data structures and algorithms.
# One of the big confusion points I had was understanding and visualizing what my code was doing. I found plenty of online tutorials that gave an answer written in C++ or Java 
# but I did not understand the answers that were presented to me. So what I did in this situation is select one answer and attempt to recreate it in Python line by line
# on my own computer. I then commented on what each code line did, to try to understand the overall program.

# (2) I was unable to figure out space/time complexity for this problem.


# RESOURCES USED
(1) https://leetcode.com/problems/maximum-average-subarray-i/description/
(2) https://www.tutorialspoint.com/maximum-average-subarray-i-in-cplusplus
(3) https://www.geeksforgeeks.org/find-maximum-average-subarray-of-k-length/
(4) https://www.youtube.com/watch?v=m-Dqu7csdJk
(5) https://www.youtube.com/watch?v=pEnY7e-5qLw
(6) https://tutorialcup.com/interview/array/find-maximum-average-subarray-of-k-length.htm
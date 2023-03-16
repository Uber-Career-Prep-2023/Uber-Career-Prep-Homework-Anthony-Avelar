# QUESTION: Given a string, reverse the order of the vowels in the string.


# PROBLEM SOLVING STRATEGY USED: Two Pointer


# TIME COMPLEXITY = ???
# SPACE COMPLEXITY = ???


# TIME SPENT: +40 minutes


# PSUEDOCODE
# Read the string given by the user
# Calculate the length of the string
# Declare variable named "reversed" to hold an empty string


# ASSUMPTIONS MADE


# ACTUAL CODE
# this function checks for vowels in upper and lower case
def isVowel(c):
    return (c=='a' or c=='A' or c=='e' or
            c=='E' or c=='i' or c=='I' or
            c=='o' or c=='O' or c=='u' or
            c=='U')


# this function does the reverse ordering of vowels
def reverseVowel(str):
    i = 0
    j = len(str) - 1
    while (i < j):
        if not isVowel(str[i]):
            i += 1
            continue
        if (not isVowel(str[j])):
            j -= 1
            continue
        
        # swapping
        str[i], str[j] = str[j], str[i]
        i += 1
        j -= 1
    return str

# REFLECTION
# (1) Same struggle as the first question of this homework. I spent the majority of my allotted 40 minutes googling the basic concepts and trying to make sense of it all.


# RESOURCES USED
# (1) https://www.geeksforgeeks.org/reverse-vowels-given-string/
# (2) https://leetcode.com/problems/reverse-vowels-of-a-string/
# (3) https://christorres09.medium.com/reverse-vowels-of-a-string-3506c94af2fb
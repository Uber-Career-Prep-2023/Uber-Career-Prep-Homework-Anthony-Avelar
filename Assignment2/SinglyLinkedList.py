'''
SinglyLinkedList.py
Anthony Avelar
Submitted 5/3/2023
First attempt at implementing Singly Linked List
'''

# QUESTION: Implement a singly linked list in Python.


# ACTUAL CODE


# Node class for each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly linked list class
class LinkedList:
    def __init__(self):
        self.head = None


    # Adding new node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Adding new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    # Inserting node in the middle
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    # Displaying the linked list
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next


# Creating a new linked list
my_list = LinkedList()

# Adding nodes to the linked list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.prepend(5)

# Displaying nodes of the linked list
my_list.display()



# REFLECTION
'''
(1) This was my first attempt ever at implementing a data structure; for the record, I haven't taken a data structures & algorithm course at my college yet.
I struggled mightily at first with interpreting the original question — the prompt was written in a vague way and mentioned several concepts I hadn't learned yet.
Ultimately I was able to write a script for the sake of turning something in, but I acknowledge that there is a lot of room for improvement with what I wrote.

(2) Before I make a second attempt, I need to invest time to throughly learn the differences between these concepts (because they kept tripping me up):
    > the concept of a class
    > the concept of an object
    > the concept of a method
    > the concept of a parameter
    > the concept of a constructor
'''

# TIME SPENT
'''
Total estimate: ~3.5 hours
~2 hours reading tutorials & retyping the code examples I saw
~1 hour writing code
~30 min testing my program
'''



# RESOURCES USED
'''
Online tutorials:
(1) https://www.geeksforgeeks.org/introduction-to-linked-list-data-structure-and-algorithm-tutorial/
(2) https://www.geeksforgeeks.org/what-is-linked-list/
(3) https://www.simplilearn.com/tutorials/data-structure-tutorial/singly-linked-list

Note: I also relied on tutoring help from one of my college professors (named Tesfaye Lemma) 
'''

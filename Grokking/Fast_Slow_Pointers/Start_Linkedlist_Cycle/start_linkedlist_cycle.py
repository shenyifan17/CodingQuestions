""""
Given the head of Singly LinkedList that contains a cycle, write a fcuntion to find 
the starting node of the cycle
"""

from __future__ import print_function 

class Node:
    """"
    This class is provided 
    """

    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 

    def print_list(self):
        temp = self 
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()
    

def find_cycle_start(head):
    """"
    head: Node class 
    """
    cycle_length = 0 
    # find the LlnkedList cycle 
    slow, fast = head, head 
    while (fast is not None and fast.next is not None):
        fast = fast.next.next 
        slow = slow.next 
        if slow == fast: # found the cycle 
            ## 3. We can find the length of the LinkedList cycle 
            ##    using the approach from "Linkedlist_cycle"
            ##    lets assume the length of the cycle is "K" nodes
            cycle_length = calculate_cycle_length(slow)
            break 
    return find_start(head, cycle_length)

def calculate_cycle_length(slow):
    current = slow 
    cycle_length = 0 
    while True:
        current = current.next 
        cycle_length += 1 
        if current == slow:
            break 
    return cycle_length 

def find_start(head, cycle_length):
    ## 1. take two pointers, call them
    ##    pointer1 and pointer2
    ## 2. initialize both pointers to the start 
    ##    of the LinkedList
    pointer1 = head 
    pointer2 = head 
    ## 4. move pointer2 ahead 'K' nodes 
    while cycle_length > 0:
        pointer2 = pointer2.next 
        cycle_length -= 1 
    # 5. Keep incrementing both pointers until they meet at the start of the cycle 
    while pointer1 != pointer2:
        pointer1 = pointer1.next 
        pointer2 = pointer2.next 
    return pointer1
        
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next 
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next 
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))    

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

main()
""""
Problem Statement:
Given the head of a Singly LinkedList, 
write a function to determine if the LinkedList has a cycle in it or not.
"""

class Node:

    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 

def has_cycle(head):
    slow, fast = head, head 
    while (fast is not None) and (fast.next is not None):
        fast = fast.next.next # fast pointer move double the speed
        slow = slow.next      # slow pointer move 1 unit
        if slow == fast:
            return True # found the circle 
    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

main()


""""
Time Complexity #
As we have concluded above, once the slow pointer enters the cycle, 
the fast pointer will meet the slow pointer in the same loop. 
Therefore, the time complexity of our algorithm will be O(N) 
where ‘N’ is the total number of nodes in the LinkedList.

Space Complexity #
The algorithm runs in constant space O(1).
"""



"""""
Extra Problem:
Given the head of a linkedlist with a cycle, find the length of the cycle 

Solution:
We can use the above solution to find the cycle in the likedlist.
Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole 
cycle with another pointer until we see the slow pointer again to find the length of 
the cycle 
"""

def find_cycle_length(head):
    slow, fast = head, head 
    while (fast is not None) and (fast.next is not None):
        ## move at different speed 
        fast = fast.next.next 
        slow = slow.next 
        if slow == fast: # found the cycle 
            return calculate_cycle_length(slow) # note "slow" as input
    return 0 

def calculate_cycle_length(slow):
    current = slow 
    cycle_length = 0
    while True: 
        current = current.next 
        cycle_length += 1 
        if current == slow: 
            break 
    return cycle_length

def main_():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

main_()
# Solution#
# The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in Reverse a LinkedList. Here are the steps we need to follow:

# Skip the first p-1 nodes, to reach the node at position p.
# Remember the node at position p-1 to be used later to connect with the reversed sub-list.
# Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
# Connect the p-1 and q+1 nodes to the reversed sub-list.

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head
    
    # after skipping 'p-1' nodes, current point will be at 'p' th node
    current, previous = head, None
    i = 0 
    while (current is not None) and (i < p-1):
        previous = current
        current = current.next 
        i += 1
    
    # We are interested in three parts of the LinkedList
    # the part before index 'p', the part between 'p' and 'q'
    # and the part after index 'q'
    last_node_of_first_part = previous 
    # after reversing the LinekdList, 'current' will becomre the last node of the 
    # sub-list
    last_node_of_sub_list = current
    #  Temporarily store the next node
    next = None

    i = 0 
    # reverse nodes between 'p' and 'q'
    while (current is not None) and (i < q - p + 1):
        next = current.next
        current.next = previous 
        previous = current
        current = next
        i += 1
    
    # connect with first part
    if last_node_of_first_part is not None:
        # 'previous' is now the first node of the sub-list
        last_node_of_first_part.next = previous 
    # this means p == 1, i.e. we are changing the first node of the LinkdeList
    else: 
        head = previous 
    
    # connect with the last part
    last_node_of_sub_list.next = current
    return head 


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 1, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

# Time complexity#
# The time complexity of our algorithm will be O(N)
# O(N)
#  where ‘N’ is the total number of nodes in the LinkedList.

# Space complexity#
# We only used constant space, therefore, the space complexity of our algorithm is O(1)
# O(1)

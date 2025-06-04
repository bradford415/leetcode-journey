from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    NOTE: the digits of each number are in reverse in the linked lists so that we can perform handwritten
          addition in a natural way; this confused me at first and I tried to do addition backwards but 
          it's actually setup so we can perform addtion in the normal way (right to left) 

    time complexity: O(n)
    space complexity: O(n)
    """
    # Create a dummy node to start the new linked list;
    # need a place to start the rover and allows us to assign the previous node.next    to the current node.next
    dummy_head = ListNode(val=0)
    rover = dummy_head

    # used to store the 10s digit
    carry = 0

    # while l1 or l2 is not None
    while l1 or l2:

        # Create the next node and assign the previous node.next to the current node
        next_node = ListNode(val=0)
        rover.next = next_node 

        val = 0
        
        # Sum the values (if they exist) and update the pointer
        if l1 is not None:
            val += l1.val
            l1 = l1.next
        if l2 is not None:
            val += l2.val
            l2 = l2.next

        val += carry

        # NOTE: we don't need to check if val >= 10 becuase if it's < 10, carry will equal 0
        carry = val // 10
        next_node.val = val % 10

        # update pointers
        rover = next_node
    
    if carry != 0:
        next_node = ListNode(val=carry, next=None)
        rover.next = next_node

    # return the node after the dummy one because this was used just as a place holder
    return dummy_head.next




if __name__ == "__main__":
    # Need to turn these into ListNodes to work
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]

    ret = addTwoNumbers(l1, l2)
    print(ret)

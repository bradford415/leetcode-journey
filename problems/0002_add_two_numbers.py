from typing import List, Optional, ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    time complexity:
    space complexity: 
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
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next

            val += carry

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
    nums = [-1,0,1,2,-1,-4]

    ret = threeSum(nums)
    print(ret)

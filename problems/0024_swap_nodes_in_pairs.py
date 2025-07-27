from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    # dummy node to mimic the a previously swapped pair before the head;
    # we'll return dummy.next when finished
    dummy = ListNode(0, next=head)

    # set prev ptr to the last node in the already swapped pair (this will let us)
    # link the two swapped pairs after swapped
    prev = dummy

    # set curr ptr to the first node in the pair to be swapped
    curr = head

    # loop while there are two nodes to swap (if there's a lone node at the end don't swap it)
    while curr and curr.next: 

        # save helper pts
        third = curr.next.next
        second = curr.next

        # swap the adjacent nodes and link the previously swapped pair
        second.next = curr
        curr.next = third
        prev.next = second

        # update the pointers for the next pair to swap
        prev = curr # the last node in the previously swapped pair
        curr = third
    
    return dummy.next



if __name__ == "__main__":

    # test cases

    ret = swapPairs()
    print(ret)

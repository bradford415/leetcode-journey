from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    rover = head

    # count the number of nodes
    list_len = 0
    while rover:
        list_len += 1
        rover = rover.next

    if list_len == 1:
        return None

    
    # need the index of the previous node to remove the link
    remove_ind = list_len - n - 1
    
    rover = head
    for i in range(remove_ind):
        rover = rover.next

    if n == 1:
        # if removing the last node, set the prev node to None
        rover.next = None
    elif n == list_len:
        # if removing the first node, return the pointer at the 2nd node
        return head.next
    else:
        # any other case set the previous node to the next next node
        rover.next = rover.next.next
    
    return head





if __name__ == "__main__":
    # Need to turn this into ListNodes to work
    #head = [1,2,3,4,5]
    n = 2

    ret = removeNthFromEnd(head, n)
    print(ret)

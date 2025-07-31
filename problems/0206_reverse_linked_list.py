from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    time complexity: O(n)
    space complexity: O(1)
    """

    curr = head
    prev = None # prev starts at last_node.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev



if __name__ == "__main__":

    # test cases

    ret = reverseList()
    print(ret)

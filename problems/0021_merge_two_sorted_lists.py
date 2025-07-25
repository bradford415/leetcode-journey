from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    time complexity: O(n + m)
        this is n+m because, in the worst case, you must vist every node at least once; for example, when
        the nodes of both lists alternate (interleaved) in values, we must vist every node to compare
        e.g., List A: 1 → 3 → 5 → 7 (m = 4)
              List B: 2 → 4 → 6 → 8 (n = 4)
    space complexity: O(1)
    """

    # create a dummy head node so we do not have to initalize the head
    # outside the loop; we'll return head->next
    head = ListNode()


    # use a rover to create the new list; allows us to keep head at the start
    # so we can return it
    rover = head

    # loop until we reach the end of one of the lists
    while list1 and list2:

        # connect list node with the lower value and move that list pointer to its next node
        if list1.val < list2.val:
            rover.next = list1
            list1 = list1.next
        else:
            rover.next = list2
            list2 = list2.next

        # move rover in both cases so we can point to the next node
        rover = rover.next

    # attach the end of the remaining (opposite list of the None list)
    if list1 is None:
        rover.next = list2
    if list2 is None:
        rover.next = list1

    # if list1:
    #     rover.next = list1
    # if list2:
    #     rover.next = list2

    # return head.next since we started with a dummy node
    return head.next


if __name__ == "__main__":
    # Need to turn this into ListNodes to work
    list1 = [1,2,4]
    list2 = [1,3,4]

    ret = mergeTwoLists(list1, list2)
    print(ret)

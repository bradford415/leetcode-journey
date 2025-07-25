from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists_brute_force(lists: List[Optional[ListNode]]):
    """
    time complexity:
    space complexity:
    """

    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]


    R = lists[0]

    for link_list in lists[1:]:

        Head = ListNode()
        H_R = Head

        R2 = link_list

        while R and R2:
            if R.val <= R2.val:
                H_R.next = R
                H_R = H_R.next
                R = R.next
            else:
                H_R.next = R2
                H_R = H_R.next
                R2 = R2.next

        if not R:
            H_R.next = R2
        elif not R2:
            H_R.next = R

        R = Head.next

    return Head.next



if __name__ == "__main__":

    # test cases

    ret = functionName()
    print(ret)

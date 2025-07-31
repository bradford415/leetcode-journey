from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    time complexity:
    space complexity:
    """

    if k == 1:
        return head
    if not head.next:
        return head

    dummy = ListNode(next=head)
    prev_set = dummy # to link the reversed group to the previous reversed group

    while True:
        # get the kth_node ptr in the group
        kth_node = self.get_kth_node(prev_set, k)

        if not kth_node:
            break

        prev = kth_node.next # last_node.next to reverse the linked list group
        curr = prev_set.next # to iterate through each node and link to prev

        # reverse the linked list group
        for i in range(k): # could also make a group_next var and say `while curr != group_next`
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        tmp2 = prev_set.next # save the location to update prev_set to 
        prev_set.next = kth_node # link previously reverse list w/ newly reversed list
        prev_set = tmp2 # update to save location of newly sorted list last_nod
    
    return dummy.next

def get_kth_node(self, curr, k):
    # finds and retunrs the postiion of the kth node in the group of k nodes
    # if curr is null first, that means the group does not have at least k nodes
    # and we won't reverse that group
    while curr and k > 0:
        curr  = curr.next
        k -= 1

    return curr


if __name__ == "__main__":

    # test cases

    ret = reverseKGroup()
    print(ret)

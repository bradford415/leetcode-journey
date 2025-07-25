from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Optimal solution; the idea is to divide and conquer such that we merge
        pairs of lists together similar to merge sort (but its not the recursive merge sort algorithm);
        we can merging two lists, reducing the len() of lists until it reaches only 1 linked list left
        then we return that list

        time complexity: O(nlog(k))
            - n is the total number of nodes across all lists (in the case like [[1, 2, 3], [4, 5, 6]] where we need to loop
              through all nodes while merging 2 lists)
            - k is the number of linked lists ("mergeKLists") and since we're halving the number of lists each time
              each node is involved in log(k) steps

        space complexity: O(k)
            - even though we're halving the number of lists stored each time, at some point its
              maximum number of lists stored is O(k) so that is the actual space complexity

        """

        if not lists:
            return None
        
        # merge pairs of lists together at a time, loop until there's only one
        # linked list left and this will be our output
        while len(lists) > 1:

            # used to store the merged lists as we merge them in pairs
            merged_lists = []
            
            # loop through 2 lists at a time to merge them (`divide and conquer`)
            for i in range(0, len(lists), 2):
                list_1 = lists[i]

                # list 2 could be out of bounds if lists is odd so we check that
                list_2 = lists[i+1] if (i+1) < len(lists) else None

                # merge the 2 lists just like the easy leetcode problem
                merged_lists.append(self.merge_2_lists(list_1, list_2))
            
            # reassign the merged_lists to the regular lists variable so we can again
            # merge the merged lists; this will repeat until len(lists) == 1
            lists = merged_lists

        return lists[0]

def merge_2_lists(self, list1, list2):
    """helper function to merge 2 lists just like the leetcode easy problem"""
    
    Head = ListNode()
    rover = Head
    R1 = list1
    R2 = list2
    while R1 and R2:
        if R1.val <= R2.val:
            rover.next = R1
            rover = rover.next
            R1 = R1.next
        else:
            rover.next = R2
            rover = rover.next
            R2 = R2.next
    
    # append the non empty list to the end of the merged array
    if R1:
        rover.next = R1
    elif R2:
        rover.next = R2
    
    return Head.next


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

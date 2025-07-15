from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST_inorder(root: Optional[TreeNode]) -> bool:
    """Create a list of inorder traversal and check if the list is sorted (with no duplicate elements)

    (a solution I came up with)

    time complexity: O(n)
    space complexity: O(n)
    """

    if not root.left and not root.right:
        return True

    inorder_vals = []

    def inorder_trav(root):

        if not root:
            return

        inorder_trav(root.left)
        inorder_vals.append(root.val)
        inorder_trav(root.right)

    inorder_trav(root)

    prev_val = inorder_vals[0]
    for val in inorder_vals[1:]:
        if val > prev_val:
            prev_val = val
        else:
            return False
    return True


def isValidBST_boundaries(root: Optional[TreeNode]) -> bool:
    """Create boundaries such that the current node value has to be less than -inf and the greater than
    positive inf; when you traverse to the left update the right boundary to the current node value and
    when you traverse to the right update the left boundary to the current node value
    """

    def valid_boundaries(root, left_bound, right_bound):

        if not root:
            return True

        if not (left_bound < root.val and right_bound > root.val):
            return False

        return (valid_boundaries(root.left, left_bound, root.val) and
        valid_boundaries(root.right, root.val, right_bound))

    is_valid = valid_boundaries(root, float("-inf"), float("inf"))

    return is_valid
    



if __name__ == "__main__":

    # test cases

    ret = isValidBST()
    print(ret)

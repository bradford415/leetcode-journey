from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def neetcode_iterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    rover = root

    # loop while the rover is not None OR the stack is not empty (still have nodes to visit);
    # i.e., we're done at the bottom right of the tree, rover = None and stack is empty
    while rover or stack:

        # loop all the way to the end of the left subtree and append to stack
        while rover:
            stack.append(rover)
            rover = rover.left

        # once we're at the end, recurse back by setting the rover equal to the
        # last stack value and vist the node (print); left->vist
        rover = stack.pop()
        result.append(rover.val)

        # move to the right to see if theres any right children, if there's not then the
        # inner while statement will not trigger and we'll keep recursing up the stack;
        # if there is a right node, will traverse all the way down the left subtree again
        rover = rover.right
    
    return result


def recursive_inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    time complexity: O(n)
        - we vist every node in the tree once
    space complexity: O(n)
        - in the worst case we have to make a recursive call (new stack) for every 
          node which may not have finished yet; in the best/average case the amount of
          recursion calls that have no completed yet are typically the height of the tree 
    """
    inorder_list = []

    def inorder(root):
        """recursive call which only takes the root node"""
        
        # base case when we've reached a leaf node
        if root == None:
            return

        # left -> right -> visit
        inorder(root.left)
        inorder_list.append(root.val)
        inorder(root.right)

    inorder(root)

    return inorder_list

    
if __name__ == "__main__":

    # test cases

    ret = recursive_inorderTraversal()
    print(ret)

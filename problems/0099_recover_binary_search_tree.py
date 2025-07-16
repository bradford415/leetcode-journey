from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(self, root: Optional[TreeNode]) -> None:
    """
    time complexity: O(n)
    space complexity: O(n)
    """

    # store the prev, first middle and last violations
    self.prev = self.first = self.middle = self.last = None

    def inorder(node):

        if not node:
            return

        inorder(node.left)

        # once prev is set, begin updating the violations
        if self.prev and not (self.prev.val < node.val) and not self.first:
            self.first = self.prev
            self.middle = node
        elif self.prev and not (self.prev.val < node.val) and self.first:
            self.last = node

        self.prev = node

        inorder(node.right)

    inorder(root)

    # if there was a non-adjacent violation, swap the first and last
    if self.last:
        temp = self.last.val
        self.last.val = self.first.val
        self.first.val = temp
    else:
        temp = self.middle.val
        self.middle.val = self.first.val
        self.first.val = temp 



if __name__ == "__main__":

    # test cases

    ret = recoverTree()
    print(ret)

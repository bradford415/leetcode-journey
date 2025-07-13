from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def __repr__(self):
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"
        


# def generateTrees(n: int) -> List[Optional[TreeNode]]:
#     """
#     time complexity:
#     space complexity:
#     """
    
#     return

    
def numTrees(n: int) -> int:
    # essentially we need to find the number of nodes for each subtree
    # so if n = 4, we have 1, 2, 3, 4 values
    # we need to compute the number of trees  in each subtree when each value is the
    # the root; so if 2 is the root, then sub tree with nodes [1], will only
    # have 1 subtree possibility, then sub tree with nodes [3, 4] will have 2 subtree
    # combinations, so the total combinations with 2 is 1 * 2 = 2; we do this for
    # every node as the root then sum up the values;
    # this is a dynamic programming problem

    # create an array of n+1 elements to store the number of trees for each number of nodes;
    # we initalize the array to 1 for the base cases 
    num_trees = [1] * (n + 1)

    # base casse:
    #   0 node = 1 tree (this is called an Empty Tree; its use for base cases in recursion and has no nodes but its still considered a tree)
    #   1 node = 1 tree

    # first loop through all the possible number of nodes that could make subtrees; 
    # if n = 5, we could have [0,1,2,3,4,5] nodes for combinations of subtrees;
    # we already have the base cases so we can skip 0 nodes and 1 nodes;
    # every iteration of this outer loop, we're updating `num_trees` at `nodes` so
    # at the end we can index with array at `n`
    for nodes in range(2, n + 1):
        total_trees = 0

        # loop through all node values so we make each one the root
        # if num_nodes = 3 then [1, 2, 3]
        for root in range(1, nodes + 1):  
            # how many nodes we'll have in the left & right subtree depending on 
            # the root
            num_left_nodes = root - 1
            num_right_nodes = nodes - root

            # number of combinations of trees from the number of tree combinations 
            # in the left and right subtrees
            total_trees += num_trees[num_left_nodes] * num_trees[num_right_nodes]

        # update the array at `nodes` with the total number of tree combinations we could make
        num_trees[nodes] = total_trees
    
    return num_trees[n]


if __name__ == "__main__":

    # test cases

    n_nodes = 5

    ret = numTrees(n_nodes)
    print(ret)

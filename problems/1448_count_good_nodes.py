from typing import List, Optional

class Solution:
    def goodNodes(self, root) -> int:
        """
        time complexity:
        space complexity:
        """

        def preorder(node, max_so_far):
            # vist - left - right
            if not node:
                return 0

            good_nodes = 0

            val = node.val
            if val >= max_so_far:
                good_nodes += 1
            new_max = max(val, max_so_far)
            good_nodes += preorder(node.left, new_max)
            good_nodes += preorder(node.right, new_max)

            return good_nodes
        
        return preorder(root, root.val)



if __name__ == "__main__":

    # test cases
    case_1 = [3,1,4,3,None,1,5]
    
    solution = Solution()

    ret = solution.goodNodes(case_1)
    print(ret)

from typing import List, Optional

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Greedy approach
        time complexity: O(n)
        space complexity: O(1)
        """

        if len(nums) == 1:
            return True

        goal_pos = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            max_jumps = nums[i]
            if max_jumps >= goal_pos - i:
                if i == 0:
                    return True
                goal_pos = i
        
        return False

    def canJump_recursion_memoization(self, nums: List[int]) -> bool:
        """Still incredibly slow and not recommended to sovle this problem
        time complexity:
            - O(n^n) wihthout memoization
            - O(n^2) with memoization
        space complexity:
        """
        
        memo = {}
        def possible_jumps(cur_pos, jumps_left):

            if jumps_left >= len(nums) - (cur_pos+1):
                return True
            
            if cur_pos in memo:
                return False

            max_jumps = nums[cur_pos]
            for i in range(1, max_jumps + 1):
                # need if statement to check all possible combinations, if we didn't have the if statement then
                # it would only check the first iteration for each call; so, `if`` one path works then we can return
                if possible_jumps(cur_pos + i, max_jumps-i):
                    return True

            # If we try all jumps and none of them lead to the end, return False
            memo[cur_pos] = False
            return False
        
        return possible_jumps(0, 0)



if __name__ == "__main__":

    # test cases
    case_1 = [2,3,1,1,4] # True
    
    solution = Solution()

    ret = solution.canJump(case_1)
    print(ret)

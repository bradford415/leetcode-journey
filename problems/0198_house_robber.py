from typing import List, Optional

class Solution:
    
    def rob(self, nums: List[int]) -> int:
    
        dp = [0] * (len(nums)+2)
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            # either take the current money and skip the next house, or don't take the money and move to the next house
            take = nums[i] + dp[i + 2]
            skip = dp[i + 1]

            dp[i] = max(take, skip)

        return dp[0]



    def rob_rec(self, nums: List[int]) -> int:

        memo = {}

        def maybe_rob(index):

            if index in memo:
                return memo[index]

            if index >= len(nums):
                return 0

            take = nums[index] + maybe_rob(index + 2)
            skip = maybe_rob(index + 1)
            memo[index] = max(take, skip)

            return max(take, skip)
    
        total = maybe_rob(0)
        return total



if __name__ == "__main__":

    # test cases
    case_1 = [2,7,9,3,1]
    
    solution = Solution()

    ret = solution.rob(case_1)
    print(ret)

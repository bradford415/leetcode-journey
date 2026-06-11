from typing import List, Optional

class Solution:
    def climbStairs(self, n: int) -> int:
        """Dynamic programming tabulation approach
        
        General idea is to start at step 0 and 1, then see how many
        ways we can get to step i, starting at step 2 up to n.

        time complexity: O(n)
        space complexity: O(n) w/ full tabulation but we only 
                          need 3 variables so we can do O(1) (not coded here)
        """
        # init dp table and base cases
        dp = [0] * (n + 1)
        
        # base cases are: how many ways to get to step 0 and step 1?
        dp[0] = 1
        dp[1] = 1

        # how many ways to get to step i is the sum of i-1 and i-2
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


    def climbStairs_memo(self, n: int) -> int:
        """
        time complexity: O(2^n) without memoization, O(n) with memoization
        space complexity: O(2^n) without memoization, O(n) with memoization
        """

        memo = {}

        def climb(num_steps):

            if num_steps in memo:
                return memo[num_steps]

            if num_steps == n:
                return 1
            elif num_steps > n:
                return 0

            if num_steps in memo:
                return memo[num_steps]

            num_ways = climb(num_steps + 1) + \
                        climb(num_steps + 2)

            memo[num_steps] = num_ways

            return num_ways

        
        all_ways = climb(0)
        return all_ways



if __name__ == "__main__":

    # test cases
    case_1 = 6
    
    solution = Solution()

    ret = solution.climbStairs(case_1)
    print(ret)

from typing import List, Optional

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]

    def change_rec(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def find_change(curr_mon, start_index):

            if (curr_mon, start_index) in memo:
                return memo[curr_mon, start_index]

            if curr_mon == amount:
                return 1

            if curr_mon > amount:
                return 0
            
            num_coins = 0
            for i in range(start_index, len(coins)):
                # passing i prevents the recursion from going backwards so we count combinations, not permutations
                num_coins += find_change(curr_mon + coins[i], i) 
            
            memo[curr_mon, start_index] = num_coins
            return num_coins
        
        return find_change(0, 0)



if __name__ == "__main__":

    # test cases
    amount = 5
    coins = [1,2,5]
    
    solution = Solution()

    ret = solution.change(amount, coins)
    print(ret)

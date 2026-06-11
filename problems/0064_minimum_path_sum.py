from typing import List, Optional

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        time complexity: O(m*n)
        space complexity:
        """
        
        num_rows = len(grid)
        num_cols = len(grid[0])

        dp = [[0] * num_cols for _ in range(num_rows)]

        # fill dp table from bottom right to top left, taking the minimum of the dp table
        # from the right and below the current cell
        for r in range(num_rows - 1, -1, -1):
            for c in range(num_cols - 1, -1, -1):
                
                if c == num_cols - 1 and r == num_rows - 1 :
                    dp[r][c] = grid[r][c]
                elif c != num_cols - 1 and r == num_rows - 1:
                    dp[r][c] = grid[r][c] + dp[r][c + 1]
                elif r != num_rows - 1 and c == num_cols - 1:
                    dp[r][c] = grid[r][c] + dp[r + 1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])

        return dp[0][0]



if __name__ == "__main__":

    # test cases
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    
    solution = Solution()

    ret = solution.minPathSum(grid)
    print(ret)

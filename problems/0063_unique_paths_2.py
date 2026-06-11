from typing import List, Optional

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        time complexity: O(m*n)
            - where m = num rows, n = num cols
        space complexity: O(m*n)
        """

        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])

        # create dp table
        dp = [[0] * num_cols for _ in range(num_rows)]

        # fill in base cases but if obstacle is foun on break case
        # everything above or left should be 0
        for i in range(num_rows-1, -1, -1):
            if obstacleGrid[i][num_cols-1] == 1:
                break
            else:
                dp[i][num_cols-1] = 1

        for i in range(num_cols-1, -1, -1):
            if obstacleGrid[num_rows-1][i] == 1:
                break
            else:
                dp[num_rows-1][i] = 1

        # standard num paths algorithm but if obstacle found set dp table to 0
        for r in range(num_rows-2, -1, -1):
            for c in range(num_cols-2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        
        return dp[0][0]



if __name__ == "__main__":

    # test cases
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    
    solution = Solution()

    ret = solution.uniquePathsWithObstacles(obstacleGrid)
    print(ret)

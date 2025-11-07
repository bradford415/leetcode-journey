from typing import List, Optional

class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        "Dyanamic programming solution - efficient"
        
        # NOTE: the finish point (bottom right of grid) starts with (0, 0)
        
        # initalize the dp table so the right and bottom edges are all 1s
        # which is the base ase
        dp = {}
        for col in range(n):
            dp[(0, col)] = 1
        for row in range(m):
            dp[(row, 0)] = 1
        
        # start at cell (1, 1) and work to (m-1, n-1);
        # the number of paths at the current cell is the sum of the paths below and to the right
        for row in range(1, m):
            for col in range(1, n):
                dp[(row, col)] = dp[(row - 1, col)] + dp[(row, col - 1)]
        
        return dp[(m-1, n-1)]
    
    def uniquePaths_recursive_slow(self, m: int, n: int) -> int:
        """Recursive solution with memoization
        time complexity:
        space complexity:
        """
        
        memo = {}

        def move_bot(pos_row, pos_col):

            if (pos_row, pos_col) in memo:
                return memo[(pos_row, pos_col)]

            if pos_row == m-1 and pos_col == n-1:
                memo[(pos_row, pos_col)] = 1
                return 1

            if pos_row >= m or pos_col >= n:
                memo[(pos_row, pos_col)] = 0
                return 0
            
            total_paths = move_bot(pos_row + 1, pos_col) +  move_bot(pos_row, pos_col + 1)

            memo[(pos_row, pos_col)] = total_paths

            return total_paths

        all_paths = move_bot(0, 0)

        return all_paths



if __name__ == "__main__":

    # test cases
    case_m = 3
    case_n = 7
    
    solution = Solution()

    ret = solution.uniquePaths(case_m, case_n)
    print(ret)

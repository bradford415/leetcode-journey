from typing import List, Optional

class Solution:
    
    def uniquePaths(self, m, n)
    
    def uniquePaths_recursive_slow(self, m: int, n: int) -> int:
        """Recursive solution with memoization but does NOT pass the time limit 
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

            return move_bot(pos_row + 1, pos_col) +  move_bot(pos_row, pos_col + 1)

        all_paths = move_bot(0, 0)

        return all_paths



if __name__ == "__main__":

    # test cases
    case_1 = 5
    
    solution = Solution()

    ret = solution.functionName(case_1)
    print(ret)

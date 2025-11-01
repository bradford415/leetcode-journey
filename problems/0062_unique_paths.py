from typing import List, Optional

class Solution:
    
    def uniquePaths(self, m, n):
        pass
    
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

    ret = solution.uniquePaths_recursive_slow(case_m, case_n)
    print(ret)

from typing import List, Optional

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_has_zero = any(matrix[r][0] == 0 for r in range(rows))

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    # set first row & col to a special character 
                    matrix[0][c] = 0
                    matrix[r][0] = 0


        # set columns to 0 if the have an "a" in the first row
        for c in range(cols-1, 0, -1):
            if matrix[0][c] == 0:
                for r in range(rows-1, -1, -1):
                    matrix[r][c] = 0

        # set rows to 0 if the have an "a" in the first col
        for r in range(rows-1, 0, -1):
            if matrix[r][0] == 0:
                for c in range(cols-1, -1, -1):
                    matrix[r][c] = 0

        if first_row_has_zero:
            for c in range(cols): # set first row to 0
                matrix[0][c] = 0
        if first_col_has_zero:
            for r in range(rows): # set first col to 0
                matrix[r][0] = 0

if __name__ == "__main__":

    # test cases
    case1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]


    
    solution = Solution()

    solution.setZeroes(case1)
    print(case1)

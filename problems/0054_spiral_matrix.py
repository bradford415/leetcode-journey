from typing import List, Optional


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        time complexity: O(m*n)
        space_complexity: O(m*n)
        
        where m = num_rows and n = num_cols
        """

        # boundary conditions, update when we added that row or column;
        # if these cross, then we're done
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        num_ele = bottom*right

        spiral_indices = []

        while left < right and top < bottom:

            # loop through top row
            for c in range(left, right):
                spiral_indices.append(matrix[top][c])
            top += 1

            # loop through right col
            for r in range(top, bottom):
                spiral_indices.append(matrix[r][right-1])
            right -= 1

            # weird edge case - so we have all the elements already, stop early
            if len(spiral_indices) == num_ele:
                break

            # loop through bottom row
            for c in range(right - 1, left - 1, -1):
                spiral_indices.append(matrix[bottom-1][c])
            bottom -= 1

            # loop through left row minus one
            for r in range(bottom - 1, top - 1, -1):
                spiral_indices.append(matrix[r][left])
            left += 1

        return spiral_indices



if __name__ == "__main__":

    # test cases
    case_1 = [[1,2,3],[4,5,6],[7,8,9]]

    solver = Solution()

    ret = solver.spiralOrder(case_1)
    print(ret)

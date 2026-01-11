from typing import List, Optional

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        time complexity:
        space complexity:
        """
    
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        max_flat_ind = num_rows * num_cols - 1

        left = 0
        right = max_flat_ind
        while left <= right:
            mid_flat_ind = (left + right) // 2
            mid_r, mid_c = self.get_2d_inds(mid_flat_ind, num_cols)

            if matrix[mid_r][mid_c] == target:
                return True
            
            # shift left or right pointer
            if matrix[mid_r][mid_c] < target:  
                left = mid_flat_ind + 1 
            elif matrix[mid_r][mid_c] > target:
                right = mid_flat_ind - 1

        return False

    # convert the flattened indices to 2d indices (row, col)
    def get_2d_inds(self, flat_ind, num_cols):
        row = flat_ind // num_cols
        col = flat_ind % num_cols
        return row, col


if __name__ == "__main__":

    # test cases
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    
    solution = Solution()

    ret = solution.searchMatrix(matrix, target)
    print(ret)

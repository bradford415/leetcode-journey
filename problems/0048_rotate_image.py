from typing import List, Optional


def rotate(matrix: List[List[int]]) -> None:
    """
    time complexity: O(n^2)
    space complexity: O(1)
        - problem required in-place
    """
    for outer_i in range(len(matrix)):
        for pos_i in range(outer_i, len(matrix)):
            matrix[outer_i][pos_i], matrix[pos_i][outer_i] = matrix[pos_i][outer_i], matrix[outer_i][pos_i]

    for row_i in range(len(matrix)):
        for col_i in range(len(matrix)//2):
            matrix[row_i][col_i], matrix[row_i][len(matrix)-col_i-1] = matrix[row_i][len(matrix)-col_i-1], matrix[row_i][col_i]

    return matrix



if __name__ == "__main__":

    # test cases
    case_1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


    ret = rotate(case_1)
    print(ret)

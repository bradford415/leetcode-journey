from typing import List, Optional


def isValidSudoku_brad(board: List[List[str]]) -> bool:
    """Solution I came up with myself, performs decently well but I think it's a brute force approach,
    need to look up a solution and compare

    time complexity:
    space complexity:
    """
    # validate rows, then columns then boxes

    squares_vals = []

    # validate rows
    for row_idx in range(len(board)):
        list_valid = []

        if row_idx % 3 == 0:
            num_squares = 0

        for col_idx in range(len(board)):

            if (col_idx) % 3 == 0 and num_squares < 3:
                squares_vals.append([])
                num_squares += 1

            cur_val = board[row_idx][col_idx]
            if cur_val != ".":
                list_valid.append(cur_val)
                squares_vals[(col_idx//3)+((row_idx//3)*3)].append(cur_val)
        
        if len(list_valid) != len(set(list_valid)):
            return False

    # validate cols
    for col_idx in range(len(board)):
        list_valid = []
        for row_idx in range(len(board)):

            cur_val = board[row_idx][col_idx]
            if cur_val != ".":
                list_valid.append(cur_val)
                #squares_vals[(row_idx//3)+(col_idx//3)].append(cur_val)

        if len(list_valid) != len(set(list_valid)):
            return False

    # validate squares
    for square in squares_vals:
        if len(square) != len(set(square)):
            return False

    return True



if __name__ == "__main__":

    # test cases
    case_1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    ret = isValidSudoku_brad(case_1)
    print(ret)

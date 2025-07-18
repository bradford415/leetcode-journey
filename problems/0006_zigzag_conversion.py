from typing import List, Optional


def convert(s: str, numRows: int) -> str:
    """
    time complexity:
    space complexity:
    """
        
    if len(s) == 1:
        return s

    result = ""

    for row_idx in range(numRows):

        # for the top & bottom row: the number of indices to move to get the next char
        increment = 2 * (numRows - 1) if numRows != 1 else 1

        for char_idx in range(row_idx, len(s), increment):
            result +=  s[char_idx]

            # for the middle rows we need the increment char and the one that appears
            # in the zigzag; if statement checks if we're in the middle rows and not out bounds
            zigzag_char_idx = increment + char_idx - 2 * row_idx
            if row_idx > 0 and row_idx < numRows-1 and zigzag_char_idx < len(s):
                result += s[zigzag_char_idx]

    return result
    



if __name__ == "__main__":

    # test cases
    case_1 = ["PAYPALISHIRING", 4]

    ret = convert(*case_1)
    print(ret)

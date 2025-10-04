from typing import List, Optional


def solveNQueens(n: int) -> List[List[str]]:
    """
    time complexity: O(n!)
        - it would be n^n but with pruning (keep track of the cols and diags) it cuts down a lot
          on the time complexity
    space complexity: O(n^2)
        - keep track of the nxn board
    """
    # keep track of where we cannot place queens
    col = set()
    neg_diag = set() # (r - c) -> formula to compute the negative diags (neg slope)
    pos_diag = set() # (r + c) -> formula to compute the positive diags (pos slope)

    # all possible solutions
    queen_loc = []

    # create a 2d board from a list of lists; each element is a row
    board = [["."] * n for _ in range(n)] 

    def place_queen_backtrack(curr_r):
        """Places queens row by row which is why we don't need
        to keep rack of the `row` the queen has been placed in
        """
        # base case: if we made it passed the last row then we have a valid board
        if curr_r == n:
            # create a copy of the board and join the rows together in the format the solution wants
            copy = ["".join(sol_row) for sol_row in board]
            queen_loc.append(copy)
            return

        # try each column for the queen
        for c in range(n):
            if c not in col and (curr_r - c) not in neg_diag and (curr_r + c) not in pos_diag:
                # if we can use this column, place queen and keep track of the
                # col and diags we used
                board[curr_r][c] = "Q"
                col.add(c)
                neg_diag.add(curr_r - c)
                pos_diag.add(curr_r + c)

                # move to the next row and try to place the next queen
                # random note: you could technically increment curr_r before the function
                #              call but then you'd have to decrement it after during backtracking;
                #              this why you'll see most solutions just do it in the function call
                place_queen_backtrack(curr_r + 1)

                # backtrack so we can find all possible solutions as well as
                # if the solution didn't work (undo what we just did)
                board[curr_r][c] = "."
                col.remove(c)
                neg_diag.remove(curr_r - c)
                pos_diag.remove(curr_r + c)
        
        # if the function makes it to here, python returns None and the code backtracks;
        # this essentially means this "path" wasn't a solution so it backtracks and tries a new one

    place_queen_backtrack(0) # begin recursive call starting at row0
                    
    return queen_loc


if __name__ == "__main__":

    # test cases
    case_1 = 4

    ret = solveNQueens(case_1)
    print(ret)

from typing import List, Optional


class Solution:
    def totalNQueens(self, n: int) -> int:
        """Same as placeNQueens except we don't need to keep track of the board
        
        
        """
        
        cols = set()
        neg_diag = set()
        pos_diag = set()
        self.valid_sols = 0

        def place_queens_backtrack(r):

            if r == n:
                self.valid_sols +=1
                return

            for c in range(n):
                if c not in cols and (r + c) not in pos_diag and (r-c) not in neg_diag:
                    cols.add(c)
                    pos_diag.add(r+c)
                    neg_diag.add(r-c)
                
                    place_queens_backtrack(r + 1)

                    cols.remove(c)
                    pos_diag.remove(r+c)
                    neg_diag.remove(r-c)
        
        place_queens_backtrack(r=0)

        return self.valid_sols


if __name__ == "__main__":

    # test cases
    case_1 = 4
    
    solution = Solution()

    ret = solution.totalNQueens(case_1)
    print(ret)

from typing import List, Optional

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        time complexity: O(n^2)
        space complexity: O(n^2)
        """
        # define boundaryies
        left, right = 0, n-1
        top, bot = 0, n-1

        # create the nxn matrix
        matrix = [[0] * n for _ in range(n)]

        # TODO: outer loop condition (while)
        num = 1
        while left <= right and top <= bot:

            # fill top row
            for i in  range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1

            # fill right col
            for i in range(top, bot+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # fill bot row
            for i in range(right, left-1, -1):
                matrix[bot][i] = num
                num += 1
            bot -= 1
            
            # fill left row
            for i in range(bot, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix



if __name__ == "__main__":

    # test cases
    case_1 = 3
    
    solution = Solution()

    ret = solution.generateMatrix(case_1)
    print(ret)

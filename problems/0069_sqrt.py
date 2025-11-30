from typing import List, Optional

class Solution:
    def mySqrt(self, x: int) -> int:
        """Binary search, if loop finishes return mid if mid*mid <= x else mid-1 since rounding down
        time complexity: O(log(n)) or technically O(log(x))
        space complexity:
        """
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1

        if mid*mid > x:
            return mid - 1
        return mid



if __name__ == "__main__":

    # test cases
    case_1 = 5
    
    solution = Solution()

    ret = solution.mySqrt(case_1)
    print(ret)

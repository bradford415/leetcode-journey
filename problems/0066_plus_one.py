from typing import List, Optional

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Loop backwards through the array and add one to the last digit.
        If 9, continue and set to 0.
        
        time complexity: O(n)
        space complexity: O(1)
        """

        for i in range(len(digits)-1, -1, -1):

            if digits[i] == 9 and i == 0:
                digits[i] = 0
                digits = [1] + digits
                break
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        return digits



if __name__ == "__main__":

    # test cases
    case_1 = [4,3,2,1]
    
    solution = Solution()

    ret = solution.plusOne(case_1)
    print(ret)

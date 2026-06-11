from typing import List, Optional

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        time complexity: O(n) - 1 pass
        space complexity: O(1) - inplace
        
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = len(nums) - 1
        i = 0
        while i <= right:

            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                continue
            i += 1



if __name__ == "__main__":

    # test cases
    case_1 = [2,0,2,1,1,0]

    solution = Solution()

    solution.sortColors(case_1)
    print(case_1)

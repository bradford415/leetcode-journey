from typing import List, Optional


class Solution:
    def maxSubArray_brute(self, nums: List[int]) -> int:
        """Brute force solution; O(n^3) time complexity"""
        
        max_subarray = [nums[0]]
        max_val = nums[0]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                inter_sum = sum(nums[i: j+1])
                if inter_sum > sum(max_subarray):
                    max_subarray = nums[i: j+1]
                    max_val = inter_sum

        return max_val


    def maxSubArray(self, nums: List[int]):
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        
        max_val = nums[0]
        running_sum = nums[0]

        for i in range(1, len(nums)):
            if running_sum < 0:
                running_sum = 0
            running_sum += nums[i]

            max_val = max(max_val, running_sum)

        return max_val


if __name__ == "__main__":

    # test cases
    case_1 = [-2,1,-3,4,-1,2,1,-5,4]
    
    solution = Solution()

    ret = solution.maxSubArray(case_1)
    print(ret)

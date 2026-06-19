from typing import List, Optional

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        time complexity:
        space complexity:
        """

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow



if __name__ == "__main__":

    # test cases
    case_1 = [1,3,4,2,2]
    
    solution = Solution()

    ret = solution.findDuplicate(case_1)
    print(ret)

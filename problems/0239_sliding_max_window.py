import collections
from typing import List, Optional


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        time complexity:
        space complexity:
        """
        
        max_arr = []
        running_queue = collections.deque()
        left = right = 0
        while right < len(nums):

            # queue has elements and the right most element is less than the one we want to add
            while running_queue and nums[running_queue[-1]] < nums[right]:
                running_queue.pop()
            running_queue.append(right)

            # if the left queue value is out of the window, remove it
            if running_queue[0] < left:
                running_queue.popleft()

            # check that we have a full window at the beginning; once we create the first full window
            # all the remaining windows will be the same size (window, not deque)
            if (right + 1) >= k:
                max_arr.append(nums[running_queue[0]])
                left += 1
            right += 1

        return max_arr 



if __name__ == "__main__":

    # test cases
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    solution = Solution()

    ret = solution.maxSlidingWindow(nums, k)
    print(ret)

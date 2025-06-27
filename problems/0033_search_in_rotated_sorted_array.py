from typing import List, Optional


def search(nums: List[int], target: int) -> int:
    """
    time complexity:
    space complexity:
    """
    L = 0
    R = len(nums) - 1
    M =  (L + R) // 2
    while L <= R:
        if nums[M] == target:
            return M

        # check if we're in the left or right sorted portion
        if nums[L] <= nums[M]: # left sorted portion
            if target > nums[M]:
                # simplest case when the array wasn't rotated (normal sorted)
                L = M + 1
            elif target < nums[L]:
                L = M + 1
            else:
                R = M - 1
        else: # right portion
            if target < nums[M]:
                R = M - 1
            elif target > nums[R]:
                R = M - 1
            else:
                L = M + 1

        M = (L + R) // 2

    return -1



if __name__ == "__main__":

    # test cases
    nums = [4,5,6,7,0,1,2]
    target = 0

    ret = search(nums, target)
    print(ret)

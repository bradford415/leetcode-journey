from typing import List, Optional


def searchRange(num: List[int], target: int) -> List[int]:
    """
    time complexity: O(log(n))
    space complexity: O(1)
        - only storing 2 indices
    """

    # find the left most index
    left_idx = bin_search(nums, target, True)

    # find the right most index
    right_idx = bin_search(nums, target, False)

    return [left_idx, right_idx]

def bin_search(nums, target, left_bias):
    """Modified binary search to continue the search until the while condition is complete
    
    left_bias = True -> search for left index; False -> search for right index
    """
    L = 0
    R = len(nums) - 1

    # index to return when the left or right target index is found
    # (-1 is the default to return if the target is not in array)
    index = -1

    while L <= R:
        M = (L + R) // 2

        if nums[M] < target:
            L = M + 1
        elif nums[M] > target:
            R = M - 1
        else:
            index = M
            if left_bias:
                R = M - 1
            else:
                L = M + 1

    return index


if __name__ == "__main__":

    # test cases
    nums = [5,7,7,8,8,10]
    target = 8

    ret = searchRange(nums, target)
    print(ret)
    
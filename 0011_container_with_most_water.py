from typing import List


def maxArea(nums: List[int], target: int) -> List[int]:
    """
    time complexity:
    space complexity:
    """
    # 
    L = 0
    R = len(height) - 1
    max_area = 0
    while L < R:

        L_val = height[L]
        R_val = height[R]

        idx_diff = R-L

        if L_val <= R_val:
            area = L_val * idx_diff
        else:
            area = R_val * idx_diff

        if area > max_area:
            max_area = area

        if L_val <= R_val:
            L += 1
        else:
            R -= 1

    return max_area



if __name__ == "__main__":

    nums = [2,7,11,15]
    target = 9

    ret = maxArea(nums, target)
    print(ret)

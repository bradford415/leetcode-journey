from typing import List


def maxArea_optimized(height: List[int]) -> List[int]:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    # two-pointer method
    # assign a left and right pointer to the start and end of the array indices;
    # start at the ends because the x-value with the potential for the highest area will be the
    # the length of the array
    L = 0
    R = len(height) - 1
    max_area = 0
    
    # loop until the left pointer meets the right pointer
    while L < R:
        L_val = height[L]
        R_val = height[R]

        idx_diff = R - L

        # take the smallest value of the left & right pointer so the 
        # water level is not diagonal
        if L_val <= R_val:
            area = L_val * idx_diff
        else:
            area = R_val * idx_diff

        # save the area if it's greater than max area
        if area > max_area:
            max_area = area

        # move the pointer which has the lowest value; we do this because the
        # pointer with the highest value has the most potential to have the highest area
        # so we want to keep it there
        if L_val <= R_val:
            L += 1
        else:
            R -= 1

    return max_area


if __name__ == "__main__":
    heights = [1,8,6,2,5,4,8,3,7]

    ret = maxArea_optimized(heights)
    print(ret)

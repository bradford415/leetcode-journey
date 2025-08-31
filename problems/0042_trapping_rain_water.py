from typing import List, Optional


def trap(height: List[int]) -> int:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
        
    max_left = height[0]
    max_right = height[-1]

    left = 0
    right = len(height) - 1

    total = 0
    curr = 1
    while left < right:
        if max_right < max_left:
            right -=1
            new_sum = max_right - height[right]
            if new_sum > 0:
                total += new_sum
            max_right = max(height[right], max_right)

        else:
            left += 1
            new_sum = max_left - height[left]
            if new_sum > 0:
                total += new_sum
            max_left = max(height[left], max_left)
        
    return total




if __name__ == "__main__":

    # test cases
    case_1 = [4,2,0,3,2,5]

    ret = trap(case_1)
    print(ret)

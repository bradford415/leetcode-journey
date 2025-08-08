from typing import List, Optional


def nextPermutation(nums: List[int]) -> None:
    """
    time complexity:
    space complexity:
    """   
    # find the "break point"
    swapped = False
    for i in range(len(nums)-2, -1, -1): # start at idx len(nums)-1
        if nums[i] < nums[i+1]:
            swapped = True
            swap_idx = i
            break

    # find the lowest number to the right of the break point and swap it with the breakpoint
    if swapped:
        min_val = nums[swap_idx + 1]
        swap_val = nums[swap_idx]
        min_idx = swap_idx + 1
        for i in range(swap_idx+1, len(nums)):
            if nums[i] <= min_val and nums[i] > swap_val: # NOTE: <= is very important here for swap numbers that are equal
                min_val = nums[i]
                min_idx = i
        
        nums[swap_idx], nums[min_idx] = nums[min_idx], nums[swap_idx]

    # reverse the elements to the right of the breakpoint to find the lowest `next` permutation;
    # if there was no break point then we want to reverse the entire array because the input was the last permutation
    if swapped:
        L = swap_idx + 1
    else:
        L = 0
    R = len(nums) - 1
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]
        L += 1
        R -= 1

    return nums
    
    return



if __name__ == "__main__":

    # test cases
    case_1 = [1, 2, 3, 3, 1, 3 ,3]

    ret = nextPermutation(case_1)
    print(ret)

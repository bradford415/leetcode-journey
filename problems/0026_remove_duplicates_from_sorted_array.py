from typing import List, Optional



def removeDuplicates_optimal(nums: List[int]) -> int:
    curr_max = nums[0]
    last_idx = 1

    for idx, val in enumerate(nums):
        if val > curr_max:
            nums[last_idx], nums[idx] = nums[idx], nums[last_idx]
            curr_max = val
            last_idx += 1
    
    return last_idx


def removeDuplicates_slower_not_inplace(nums: List[int]) -> int:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    
    unique_dict = {}
    for idx, val in enumerate(nums):
        if val not in unique_dict:
            unique_dict[val] = idx
    
    for nums_idx, (val, idx) in enumerate(unique_dict.items()):
        if val != nums[nums_idx]:
            nums[nums_idx], nums[idx] = nums[idx], nums[nums_idx]
    
    return len(unique_dict.keys())



if __name__ == "__main__":

    # test cases
    case_1 = [0,0,1,1,1,2,2,3,3,4]

    ret = removeDuplicates_optimal(case_1)
    print(case_1[:ret])

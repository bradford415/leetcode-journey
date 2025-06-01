from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    time complexity: O(n^2)
    space complexity: O(1)
        - the only variables used are i & j which store single integers
          the space does not scale with the input length
    """

    # loop through the entire array as the first pointer
    for i in range(len(nums)):
        # define a second pointer j that starts at i + 1 and loop through the end of the array;
        # since we can only use one element one, the first pointer does not need to be checked
        # again by the 2nd pointer
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum_fast(nums: List[int], target: int) -> List[int]:
    """
    time complexity: O(n)
    space complexity: O(n)
        - the only variables used are i & j which store single integers
          the space does not scale with the input length
    """

    # build a dictionary of: keys = array value s and values = index of values
    vals_idx_dict = {}
    for i in range(len(nums)):
        cur_val = nums[i]
        vals_idx_dict[cur_val] = i

    # loop through the array once and find calculate the value that would sum to the target;
    # index the hashmap at this value and, if it exists AND the current index != hash_map_index,
    # then we found the two indices and can return the solution
    for i in range(len(nums)):
        cur_val = nums[i]
        need_val = target - cur_val

        if need_val in vals_idx_dict:
            need_idx = vals_idx_dict[need_val]
            return [i, need_idx]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    ret = twoSum_fast(nums, target)
    print(ret)

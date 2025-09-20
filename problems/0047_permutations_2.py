from typing import List, Optional
from collections import defaultdict


def permuteUnique(nums: List[int]) -> List[List[int]]:
    """
    time complexity: O(n * n!)
        - n for the copy() and there are at most n! permutations
    space complexity: O(n * n!)
        - each permutation takes n space and there can be at most n! permuations to store
    """

    uniq_perms = []
    count_map = defaultdict(int)
    for num in nums:
        count_map[num] += 1

    def dfs(curr_comb):

        if len(curr_comb) == len(nums):
            uniq_perms.append(curr_comb.copy())
            return
        
        for key in count_map:
            if count_map[key] > 0:
                curr_comb.append(key)
                count_map[key] -= 1
                
                dfs(curr_comb)

                # backtrack; undo what we did above
                count_map[key] += 1
                curr_comb.pop()
    dfs([])

    return uniq_perms


if __name__ == "__main__":

    # test cases
    nums = [1,1,2]


    #ret = solve.jump_recursive(nums)
    ret = permuteUnique(nums)
    print(ret)

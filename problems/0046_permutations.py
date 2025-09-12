from typing import List, Optional


def permute(nums: List[int]) -> List[List[int]]:
    """This diagram is the gold standard for the permuation explanation:
    https://www.geeksforgeeks.org/dsa/write-a-c-program-to-print-all-permutations-of-a-given-string/

    time complexity: O(2^n)
    space complexity: O(n*2^n)
    """

    all_combs = []

    def find_perms(fixed_i):

        if fixed_i == len(nums) - 1: # -1 bc we don't need to swap the last element
            all_combs.append(nums.copy())
            return

        for idx in range(fixed_i, len(nums)):
            # each level in the recursion tree we want to "fix" the next element which means it cannot be swapped;
            # at each level, we want to swap the first non-fixed element with all other elements
            # each recrusive call we're performing a dfs on each branch
            nums[fixed_i], nums[idx] = nums[idx], nums[fixed_i]
            find_perms(fixed_i + 1)

            # backtrack by undoing swap; at each recursion branch, we want to start from scratch
            nums[fixed_i], nums[idx] = nums[idx], nums[fixed_i]

    find_perms(0)

    return all_combs


if __name__ == "__main__":

    # test cases
    nums = [1, 2, 3]

    #ret = solve.jump_recursive(nums)
    ret = permute(nums)
    print(ret)

from typing import List, Optional


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    time complexity: O(n * 2^n)
        - n for copying the correct combination each time nad 2^n because at each index of 
        candidates we'll have two decisions to make (2 recursive calls) and we have to explore each index n
        so the recursion depth is worst case 2^n
    space complexity: O(k*n + n)
    """

    all_combs = []

    def find_combs(idx, curr_comb, total):

        if total == target:
            all_combs.append(curr_comb.copy()) # DON'T FORGET COPY
            return
        if total > target or idx >= len(candidates):
            return
        

        # include candidates[idx]
        curr_comb.append(candidates[idx])
        find_combs(idx+1, curr_comb, total + candidates[idx]) # cannot just pass i because we cannot reuse the same element like in combination sum 1
        curr_comb.pop()

        # skip candidates[i]
        # loop until we reach the end of the sorted lists duplicates so 
        # we don't reuse the same number, since we need combinations and not permutations
        # e.g., [1, 1, 1, 1 (loop till here), 3, 5, 8]
        # first condition prevents index out of bounds error
        while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
            idx += 1
        
        find_combs(idx+1, curr_comb, total)

    # sort list so we can skip the duplicates after the first combination recurision
    candidates.sort()

    find_combs(0, [], 0)

    return all_combs



if __name__ == "__main__":

    # test cases
    case_1 = [10,1,2,7,6,1,5]
    target_1 = 8

    ret = combinationSum2(case_1, target_1)
    print(ret)

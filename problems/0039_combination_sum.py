from typing import List, Optional


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    time complexity: O(2^target)
        - recursive solution with 2 subtrees and the smallest candidate value can be 1,
          so the worst case is that we have to recurse 7 times (height of our reursion tree)
    """
    
    all_combs = []

    def dfs(total, idx, curr_comb):

        if total == target: # base case if we found a valid combination
            # NOTE: since we're only using 1 list to keep track of all combinations,
            # we need to append a copy so we don't modify the already found combinations
            all_combs.append(curr_comb.copy()) 
            return
        if idx >= len(candidates) or total > target:
            return

        val = candidates[idx]
        curr_comb.append(val)

        # recurse down the left decision subtree which can contain any value
        dfs(total + val, idx, curr_comb)

        # pop the last val added before we go down the other decision tree
        # prevents us from including a permutation
        curr_comb.pop() 

        # recurse down the right decision subtree;
        # i + 1 indicates we cannot include candidate[i] in out combination
        # which prevents permuations
        dfs(total, idx+1, curr_comb) 

    dfs(0, 0, [])

    return all_combs



if __name__ == "__main__":

    # test cases
    case_1 = [2,3,5]
    target_1 = 8

    ret = combinationSum(case_1, target_1)
    print(ret)

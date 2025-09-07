from typing import List, Optional


def isMatch(s: str, p: str) -> bool:
    """
    time complexity:
    space complexity:
    """
    # cache for memoization - saves function states so we do not need to recurse 
    # if we've already computed the value
    memo = {}
    
    def all_matches(str_i, pat_j, text, pattern):

        # check cache before recomputing everything - memoization
        if (str_i, pat_j) in memo:   
            return memo[(str_i, pat_j)]

        # first 3 if statements are the exhaustion cases
        # exhausted = we've reached the end and there's nothing left

        # if we've exhausted both the s and p and nothing is left to check
        if str_i < 0 and pat_j < 0:
            memo[(str_i, pat_j)] = True
            return True

        # if the string is exhausted (nothing left to check) and the
        # pattern still has characters left to match, then the match failed
        if str_i >= 0 and pat_j < 0:
            memo[(str_i, pat_j)] = False
            return False

        # if we've exhausted the pattern but not the string
        if str_i < 0 and pat_j >= 0:
            for remaining_i in range(pat_j+1):
                if pattern[remaining_i] != "*":
                    memo[(str_i, pat_j)] = False
                    return False

            memo[(str_i, pat_j)] = True
            return True

        if text[str_i] == pattern[pat_j] or pattern[pat_j] == "?":
            ans =  all_matches(str_i - 1, pat_j - 1, text, pattern)
            memo[(str_i, pat_j)] = ans
            return ans

        if pattern[pat_j] == "*":
            ans = (all_matches(str_i, pat_j-1, text, pattern)
                or all_matches(str_i-1, pat_j, text, pattern))
            memo[(str_i, pat_j)] = ans
            return ans

        memo[(str_i, pat_j)] = False
        return False

    return all_matches(len(s)-1, len(p)-1, s, p)
            

if __name__ == "__main__":

    # test cases
    s = "cb"
    p = "?a"

    ret = isMatch(s, p)
    print(ret)

from typing import List, Optional
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        time complexity: O(n + m)
        space complexity: O(m) or O(k)/O(1) where kis the alaphabet size
        """

        # edge case
        if t == "": 
            return ""

        # build a count dict of the letters in t and a place to store the window subtring count
        t_count = defaultdict(int)
        win_count = {}
        for char in t:
            t_count[char] += 1 
            win_count[char] = 0

        left = 0 # only need left since the for loop controls right
        have, need = 0, len(t_count.keys())
        abs_min, abs_max = -1, -1
        res_length =  float('inf')

        for right in range(len(s)):

            if s[right] in win_count:
                win_count[s[right]] += 1

            if s[right] in win_count and win_count[s[right]] == t_count[s[right]]:
                have += 1

            while have == need:
                # update the result bounds
                if (right - left + 1) < res_length:
                    abs_max, abs_min = right, left
                    res_length = right - left + 1

                if s[left] in win_count:
                    win_count[s[left]] -= 1
                    if win_count[s[left]] < t_count[s[left]]:
                        have -= 1
                left += 1

        return s[abs_min: abs_max+1] 



if __name__ == "__main__":

    # test cases
    s = "ADOBECODEBANC"
    t = "ABC"
    
    solution = Solution()

    ret = solution.minWindow(s, t)
    print(ret)

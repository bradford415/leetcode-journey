from typing import List, Optional

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        time complexity: O(n)
        space complexity: O(k)
            - where k is the length of the separators
        """
        last_word = s.split()[-1]

        return len(last_word)



if __name__ == "__main__":

    # test cases
    case_1 = "   fly me   to   the moon "
    
    solution = Solution()

    ret = solution.lengthOfLastWord(case_1)
    print(ret)

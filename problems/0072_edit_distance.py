from typing import List, Optional

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        """
        
        dp_table = [[0] * (len(word2) + 1) for _ in  range(len(word1) + 1)]
        
        for i in range(len(word2) + 1):
            dp_table[-1][i] = len(word2) - i
        
        for i in range(len(word1) + 1):
            dp_table[i][-1] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp_table[i][j] = dp_table[i+1][j+1]
                else:
                    dp_table[i][j] = min(dp_table[i+1][j], dp_table[i][j+1], dp_table[i+1][j+1]) + 1

        return dp_table[0][0]


if __name__ == "__main__":

    # test cases
    word1 = "intention"
    word2 = "execution"
    
    solution = Solution()

    ret = solution.minDistance(word1, word2)
    print(ret)

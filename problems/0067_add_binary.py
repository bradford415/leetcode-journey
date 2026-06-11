from typing import List, Optional

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        
        top = a if len(a) >= len(b) else b
        bot = b if len(a) >= len(b) else a

        top = top[::-1]
        bot = bot[::-1]

        bin_sum = ""

        carry = 0
        for i in range(len(top)):

            bot_val = int(bot[i]) if i < len(bot) else 0

            digit_sum = int(top[i]) + bot_val + carry

            carry = digit_sum // 2

            bin_sum = str(digit_sum % 2) + bin_sum
        
        if carry == 1:
            bin_sum = "1" + bin_sum

        return bin_sum 



if __name__ == "__main__":

    # test cases
    a = "1010"
    b = "1011"
    
    solution = Solution()

    ret = solution.addBinary(a, b)
    print(ret)

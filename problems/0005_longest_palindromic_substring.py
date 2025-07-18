from typing import List, Optional


def longestPalindrome(s: str) -> str:
    """
    time complexity: O(n^2)
    space complexity: O(1)
    """

    longest_p_str = ""

    for i in range(len(s)):

        # check the case where the palindrome is odd
        L = i
        R = i
        while L >= 0 and R < len(s):
            if s[L] == s[R]:

                cur_s = s[L: R+1]

                if len(cur_s) > len(longest_p_str):
                    longest_p_str = cur_s

                L -= 1
                R += 1
            else:
                break

        # check the case where the palindrome is odd
        L = i - 1
        R = i
        while L >= 0 and R < len(s):
            if s[L] == s[R]:
                
                cur_s = s[L: R+1]

                if len(cur_s) > len(longest_p_str):
                    longest_p_str = cur_s

                L -= 1
                R += 1
            else:
                break

    return longest_p_str
    

def longestPalindrome_sw_lr_pointers(self, s: str) -> str:
    """Using a sliding window and and L/R pointers is the same time complexity as the brute force
    sadly 
        time complexity: O(n^3)
        space complexity: O(1)
    """
    
    window_size = len(s)
    while window_size != 0:
        for i in range(len(s) - window_size + 1):

            L = i
            R = window_size - 1 + i
            while L <= R:
                if s[L] == s[R]:
                    L += 1
                    R -= 1
                else:
                    break
                if L >= R:
                    return s[i:window_size+i]

        window_size -= 1

if __name__ == "__main__":

    # test cases
    test_1 = "babad"

    ret = longestPalindrome(test_1)
    print(ret)

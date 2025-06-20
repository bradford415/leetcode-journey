from typing import List, Optional


def letterCombinations(digits: str) -> List[str]:
    """
    time complexity: O(n4^n)
        - Each combination will have at most 4 leters we need to search (7 or 9) and each combination
          will be n=len(digits), so we'll have at most 4^n recursive calls and for each call we're building a 
          string of length n so we need to multiply by n
        - for example the worst case could be digits=9999 -> we have 4 combinations for each 4*4*4*4 = 4^n
          and len(digits) = n -> n*4^n
    space complexity:
    """

    digit_to_number = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    combos = []

    def rec_call(digit_idx, cur_str):

        # base case: once we have the correct number of digits for a combination;
        #            the maximum number of digits per combination is the len(digits)
        if len(digits) == len(cur_str):
            # append the combination to the list once its finished
            combos.append(cur_str)
            return

        # map the current digit to the group of letters
        digit_group = digit_to_number[digits[digit_idx]]

        # loop through every char in the group (this will start off a recursive call for each character in the first group)
        for char in digit_group:
            rec_call(digit_idx + 1, cur_str + char)

    # being recursive call; we need the if statement bc if digits=""
    # the recursive call would give [""] but the problem wants []
    if digits:
        rec_call(0, "")

    return combos
                



if __name__ == "__main__":
    
    digits = "23"

    ret = letterCombinations(digits)
    
    print(ret)

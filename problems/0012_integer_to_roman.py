from typing import Optional


def intToRoman(num: int) -> str:
    """
    time complexity: O(1)
        - we only need to loop over the map which is always a constant size and doesn't grow based
        - on the num size
    space complexity: O(1)
        - this is only constant space since the problem contrains the num <= 3999 so there can be
          only ~15 roman numers; if this was not capped then it would be O(n) I believe
    """
    # Create a map of the given table and also add the special cases (900, 400, 90, 40, etc...)
    # NOTE: I used a list of lists to preserve order but I found out dicts in python 3.7 guarantee 
    rn_map = [
        [1000,"M"],
        [900,"CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"],
    ]

    # empty string to build the resulting string
    numeral = ""

    # Loop through the highest roman numerals first since that's how we represent roman numerals
    for r_num, roman, in rn_map:
        
        # use integer division to figure out how many symbols we need 
        # (e.g., 3794 // 1000 = 3 -> 3  Ms)
        num_lettters = num // r_num
        
        # build the string for this position of the number 
        # (the next 2nd iteration will be 794//900 = 0 so it will append an empty string 
        # which does nothing, this is why we don't need to account for edge cases)
        numeral += roman * num_lettters
         
        # use the remainder to update the number (3794 -> 794)
        num %= r_num
    
    return numeral
         
        


if __name__ == "__main__":
    
    num = 3749

    ret = intToRoman(num)
    
    print(ret)

from typing import Optional


def romanToInt(s: int) -> str:
    """
    time complexity:
    space complexity:
    """
    rn_map = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    
    full_number = 0
    
    # Loop through the string and check 2 characters at a time; if there's no match with 
    # two characters (the special cases), then only check the first character;
    # if the special case matches, increment idx twice since we already used two characters
    # but if we only match the first character, increment once
    # NOTE: I recently found out in a python for loop if you increment the index variable 
    #       inside the loop, it does not affect the index counter which ends the loop 
    #       (almost like it's its own scope); this is why I used a while loop
    idx = 0
    while idx < len(s):

        # check 2 characters at a time
        chars = s[idx:idx+2] # + 2 since the second value is exclusive (checks [0] & [1])

        if chars in rn_map:
            full_number += rn_map[chars]
            idx += 2 # skip the next 2 characters since they were used
        else:
            full_number += rn_map[chars[0]]
            idx += 1 # skip only one character since we only used 1
    
    return full_number
         
        


if __name__ == "__main__":
    
    s = "MCMXCIV"

    ret = romanToInt(s)
    
    print(ret)

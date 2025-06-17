from typing import Optional


def intToRoman(num: int) -> str:
    """
    time complexity:
    space complexity:
    """
    rn_map = {
        1000: "M",
        500: "D",
        100: "C",
        50: "L",
        10: "X",
        5: "V",
        1: "I"
    }

    numeral = ""

    temp_num = num
    for key, val in rn_map.items():

        digit = temp_num // key

        while temp_num > 0:

            if digit == 4:
                breakpoint()
                temp_num -= 4*key
                numeral += rn_map[key]
                numeral += rn_map[4*key+key]
                break
            elif digit == 9:
                temp_num -= 9*key
                numeral += rn_map[key]
                numeral += rn_map[9*key+key]
                break
            elif temp_num - key >= 0:
                temp_num -= key
                numeral += rn_map[key]
            else:
                break

    return numeral

if __name__ == "__main__":
    
    num = 3749

    ret = intToRoman(num)
    
    print(ret)

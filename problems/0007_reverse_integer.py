import math
from typing import List, Optional


def reverse(x: int) -> int:
    """
    time complexity:
    space complexity:
    """
    
    MIN = -2**31
    MAX = 2**31 - 1

    result_num = 0
    while x != 0:
        # mod of negative will give a weird answer so we can use python math.fmod
        # need int() because it returns float for some reason
        digit = int(math.fmod(x, 10))

        # python doesn't hanndle integer division of negatives well (-1 // 10 = -1 but should be 0)
        x = int(x / 10)

        if result_num > MAX // 10 or (result_num == MAX // 10 and digit > MAX % 10):
            return 0
        elif result_num < MIN // 10 or (result_num == MIN // 10 and digit < MIN % 10):
            return 0
        else:
            result_num = result_num*10 + digit   

    return result_num



if __name__ == "__main__":

    # test cases
    case_1 = -9
    case_2 = 0
    case_3 = 321

    ret = reverse(case_3)
    print(ret)

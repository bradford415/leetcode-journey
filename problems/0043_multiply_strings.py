from typing import List, Optional


def multiply(num1: str, num2: str) -> str:
    """
    time complexity:
    space complexity:
    """

    num1 = str_to_int(num1)
    num2 = str_to_int(num2)

    prod = num1*num2

    return int_to_str(prod)

def str_to_int(str_num):
    digit_ind = 0
    final_num = 0
    for idx in range(len(str_num), 0, -1):
        ascii_dig = ord(str_num[idx-1]) - 48
        final_num += ascii_dig * 10 ** digit_ind
        digit_ind += 1

    return final_num 

def int_to_str(int_num):

    if int_num == 0:
        final_str = "0"
    else:
        final_str = ""

    while int_num > 0:
        dig = int_num % 10
        int_num //= 10
        final_str = chr(dig + 48) + final_str

    return final_str



if __name__ == "__main__":

    # test cases
    num1 = "123"
    num2 = "456"

    ret = multiply(num1, num2)
    print(ret)

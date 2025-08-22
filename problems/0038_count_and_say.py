from typing import List, Optional


def countAndSay(n: int) -> str:
    """
    time complexity:
    space complexity:
    """

        
    if n == 1:
        return "1"
    if n == 2:
        return "11" 
    
    seq = "11"
    idx = 1
    while idx < n-1:
        last_num = seq[0]
        left = 0
        new_seq = ""
        for right in range(1, len(seq)):
            if seq[right] != last_num:
                new_seq += _say_nums(seq[left:right], last_num)
                left = right
                last_num = seq[left]

        new_seq += _say_nums(seq[left:], last_num)

        seq = new_seq
        idx += 1
    
    return new_seq

def _say_nums(nums, num):
    return str(len(nums)) + num

    



if __name__ == "__main__":

    # test cases
    case_1 = 4

    ret = countAndSay(case_1)
    print(ret)

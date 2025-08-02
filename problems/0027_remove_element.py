from typing import List, Optional


def removeElement(nums: List[int], val: int) -> int:
    """
    time complexity:
    space complexity:
    """
    k = 0 
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[k] = nums[k], nums[i]
            k += 1

    return k
    

if __name__ == "__main__":

    # test cases
    case_1 = [0, 1, 2, 2, 3, 2, 0, 4, 2]
    val = 2

    ret = removeElement(case_1, val)
    print(case_1[:ret])

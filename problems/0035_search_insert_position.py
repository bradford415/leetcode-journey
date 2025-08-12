

def searchInsert(nums: list[int], target):
    """
    time complexity:
    space complexity:
    """
    L = 0
    R = len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            L = mid + 1
        elif nums[mid] > target:
            R = mid - 1

    return L
    

if __name__ == "__main__":

    # test cases
    case_1 = [1,3,5,6]
    target_1 = 2

    ret = searchInsert(case_1, target_1)
    print(ret)

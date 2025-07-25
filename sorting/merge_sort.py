

def merge(left_array, right_array, array):
    """Auxiliary function to merge two subarrays in sorted order"""

    l_idx = 0
    r_idx = 0
    full_idx = 0
    while l_idx < len(left_array) and r_idx < len(right_array):
        if left_array[l_idx] <= right_array[r_idx]:
            array[full_idx] = left_array[l_idx]
            l_idx += 1
        else:
            array[full_idx] = right_array[r_idx]
            r_idx += 1
        full_idx += 1

    while l_idx < len(left_array):
        array[full_idx] = left_array[l_idx]
        l_idx += 1
        full_idx += 1

    while r_idx < len(right_array):
        array[full_idx] = right_array[r_idx]
        r_idx += 1
        full_idx += 1


def merge_sort(subarray):
    """Recursive merge sort call"""

    if len(subarray) == 1:
        return 

    
    mid = (len(subarray) - 1) // 2

    left_array = subarray[: mid+1]
    right_array = subarray[mid+1:]

    merge_sort(left_array) # left
    merge_sort(right_array) # right
    merge(left_array, right_array, subarray)

if __name__ == "__main__":
    
    vals = [3, 7, 8, 5, 4, 2, 6, 1]

    merge_sort(vals)

    print(vals)

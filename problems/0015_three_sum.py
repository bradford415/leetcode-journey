from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """NOTE: the optimal solution is pretty confuing and I'd recommend looking at NeetCode video
             if you need a refresher on how it works

    time complexity: O(nlog(n)) + O(n^2) [sorting + (O(n^2))]
    space complexity: 
    """
    
    nums = sorted(nums)

    triplets = []
    for x_idx in range(len(nums)):
        x = nums[x_idx]

        if x_idx > 0 and nums[x_idx-1] == x:
            continue

        L_idx = x_idx+1
        R_idx = len(nums) - 1
        while L_idx < R_idx:
            y = nums[L_idx]
            z = nums[R_idx]
            tot_sum = x + y + z

            if tot_sum > 0:
                R_idx -= 1
            elif tot_sum < 0 :
                L_idx +=1
            else:
                triplets.append([x, y, z])
                # NOTE: do not break because the L & R pointers can still find additional solutions for the same x value
                # We need to update the L or R pointer (and the other will update automatically by the previous condition)
                # We need to update one of the pointers because there could be duplicate value similarily how we checked for the x value at the start of the for loop
                L_idx += 1
                while nums[L_idx] == nums[L_idx-1] and L_idx < R_idx:
                    L_idx += 1

    return triplets




if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]

    ret = threeSum(nums)
    print(ret)

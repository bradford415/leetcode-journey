from typing import List, Optional

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        """
            time complexity:
            space complexity:
        """
        max_consecutive = 0

        nums_set = set(nums) # O(n)
        for num in nums_set:
            # MAKE SURE TO LOOP THROUHG NUMS_SET AND NOT NUMS SINCE NUMS CAN CONTAIN DUPLICATES WHICH WE WANT TO IGNORE 

            # check if we're at the beginning of a sequence
            if num - 1 not in nums_set:

                # count the sequence
                curr_consecutive = 1
                while num + 1 in nums_set:
                    curr_consecutive += 1
                    num += 1

                max_consecutive = max(max_consecutive, curr_consecutive)

        return max_consecutive



if __name__ == "__main__":

    # test cases
    case_1 = 5
    
    solution = Solution()

    ret = solution.functionName(case_1)
    print(ret)

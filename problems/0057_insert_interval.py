from typing import List, Optional

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        time complexity: O(n)
        space complexity:
        """
        
        merged_ints = []
        for int_i in range(len(intervals)):
            if newInterval[1] < intervals[int_i][0]:
                # if the max of the new interval is lower than the first minimum
                # we can just prepend the new interval and return;
                # NOTE: this isn't just for the beginning, it also works in the middle of the 
                #       array since the other conditionals will merge the preceeding ones
                merged_ints.append(newInterval)
                return merged_ints + intervals[int_i:]
            elif newInterval[0] > intervals[int_i][1]:
                # if the min of the new interval is greater than the max of the current one
                # we only want to append the current interval, not the new interval YET because
                # it can still be overlapping with future ones
                merged_ints.append(intervals[int_i])
            else:
                # merge the intervals
                newInterval = [min(newInterval[0], intervals[int_i][0]), max(newInterval[1], intervals[int_i][1])]
            
        # append the merged interval at the very end (if the first if does not trigger since it has a return)
        merged_ints.append(newInterval)
        return merged_ints



if __name__ == "__main__":

    # test cases
    case_1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    
    solution = Solution()

    ret = solution.insert(case_1, new_interval)
    print(ret)

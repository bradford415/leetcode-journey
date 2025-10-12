from typing import List, Optional

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        time complexity: O(nlog(n))
            - sort then iterate once through list
        space complexity:
            - O(n)
        """

        # sort the list of intervals by the start of each interval in ascending order
        intervals.sort(key = lambda x: x[0])

        merged_intervals = [intervals[0]]
        for int_i in intervals[1:]:
            
            if int_i[0] <= merged_intervals[-1][1]:
                combine = merged_intervals[-1] + int_i
                
                # we technically don't need to take min since we sorted by it at the start 
                merged_intervals[-1] = [min(combine), max(combine)] 
            else:
                merged_intervals.append(int_i)

        return merged_intervals



if __name__ == "__main__":

    # test cases
    case_1 = [[1,3],[2,6],[8,10],[15,18]]
    
    solution = Solution()

    ret = solution.merge(case_1)
    print(ret)

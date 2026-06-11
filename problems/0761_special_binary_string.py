from typing import List, Optional

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        time complexity: O(n^2)
        space complexity: O(n^2)
        """
    
        def find_spec_strs(sub_str):
            
            # base case: if the sub string is empty because we constantly strip 1s and 0s
            if not sub_str:
                return ""
            
            counter = 0
            sub_strs = []
            start_ind = 0
            for ind in range(len(sub_str)):
                if sub_str[ind] == "1":
                    counter += 1
                if sub_str[ind] == "0":
                    counter -= 1
                if counter == 0:
                    
                    # grab the current string we're looking at so far in the loop
                    current_str = sub_str[start_ind: ind+1]
                    
                    # strip lead 1 and trailing 0
                    inner_part = current_str[1: -1]

                    # recurse and append the leading 1 and trailing 0 back                    
                    optimized_sub_s = "1" + find_spec_strs(inner_part) + "0"
                    
                    # save the optimized sub string
                    sub_strs.append(optimized_sub_s)
                    start_ind = ind + 1
            
            return "".join(sorted(sub_strs, reverse=True))
        
        return find_spec_strs(s)
        

if __name__ == "__main__":

    # test cases
    case_1 = "11011000"
    case_2 = "101010"
    
    solution = Solution()

    ret = solution.makeLargestSpecial(case_1)
    print(ret)

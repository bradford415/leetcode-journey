from typing import List, Optional

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        result = []

        def backtrack(index, parts):

            # basecases: must be split into 4 parts
            if len(parts) == 4:
                if index == len(s): # must consume the entire string
                    result.append(".".join(parts))

                # after reach 4 parts, always stop this branch so the left over digits don't keep running
                return 

            for length in range(1,4):
                
                # check if the segment exists before we access it; 
                # use break because any length after this one will also break
                if index + length > len(s):
                    break

                seg = s[index: index+length]
                
                if length > 1 and seg[0] == "0":
                    continue
                if int(seg) > 255:
                    continue
                parts.append(seg) # cannot pass this directly into the function because it returns None
                backtrack(index + length, parts)
                parts.pop()

        backtrack(0, [])

        return result



if __name__ == "__main__":

    # test cases
    case_1 = "101023"
    
    solution = Solution()

    ret = solution.restoreIpAddresses(case_1)
    print(ret)

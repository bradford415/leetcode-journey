from typing import List, Optional

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        # append a trailing slash so we know when to stop since not all inputs have one
        path += "/"

        dir_name = ""
        for i in range(len(path)):

            if path[i] == "/":
                if dir_name == "..":
                    # CANNOT COMBINE THESE IF STATEMENTS; if we did adn the stack is empty it will trigger
                    # the elif
                    if stack:
                        stack.pop()
                elif dir_name != "." and dir_name != "": # "" handles the multiple slashes case e.g., "////"
                    stack.append(dir_name)
                dir_name = ""
            else:
                dir_name += path[i]

        return "/" + "/".join(stack)


if __name__ == "__main__":

    # test cases
    case_1 = "/home/user/Documents/../Pictures"
    
    solution = Solution()

    ret = solution.simplifyPath(case_1)
    print(ret)

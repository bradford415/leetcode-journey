from typing import List, Optional


def isValid_iterative(s: str) -> bool:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    matches = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    stack = []

    for char in s:

        if char in matches:
            if stack:
                c_match = stack.pop()
                if c_match not in matches.values():
                    return False
                if c_match != matches[char]:
                    return False
            else:
                return False
        else:
            stack.append(char)
    
    if not stack:
        return True
    else:
        return False



if __name__ == "__main__":

    # test cases
    case_1 = "([])"
    case_2 = "([]}"

    ret = isValid_iterative(case_2)
    print(ret)

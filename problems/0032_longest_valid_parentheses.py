from typing import List, Optional


def longestValidParentheses(s: str):
    """Perform a normal valid parentheses stack but push indices onto stack, if it's valid, then the stack
    should be empty and we can count the max length with index - stack[-1] (because it should be 0 or -1) if it's invalid, 
    save the index and continue; this invalid index will act as the new starting point to start counting the substring again
    """

    stack = [-1]
    max_length = 0

    # build the stack a
    for i,char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i-stack[-1])
    return max_length


def longestValidParentheses_high_memory(s: str) -> int:
    """Some high memory solution I came up with on my own (not optimal)

    time complexity:
    space complexity:
    """
    paren_stack = []
    idx_stack = []
    valid_parens = [] # keep track of open parens

    for index, val in enumerate(s):

        if val == "(":
            paren_stack.append(val)
            idx_stack.append(index)
            valid_parens.append(0)
        elif val == ")":
            valid_parens.append(0)
            if not paren_stack:
                continue
            top_val = paren_stack.pop()
            top_idx = idx_stack.pop()
            valid_parens[index] = 1
            valid_parens[top_idx] = 1

    longest_substring = 0
    running_sum = 0
    for val in valid_parens:
        if val > 0:
            running_sum += val
        else:
            if running_sum > longest_substring:
                longest_substring = running_sum
            running_sum = 0
        if running_sum > longest_substring:
            longest_substring = running_sum

    return longest_substring



if __name__ == "__main__":

    # test cases
    case_1 = ")()())"

    ret = longestValidParentheses(case_1)
    print(ret)

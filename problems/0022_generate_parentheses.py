from typing import List, Optional



def generateParenthesis_neetcode(n: int) -> List[str]:
    """Neetcode solution; basically the same but he uses global stack
    time complexity:
    space complexity:
    """
    
    # stores all valid pairs once found
    valid_parens = []

    # used to build the parentheses pairs
    stack = []

    def backtrack(num_open, num_close):

        # only add open ( if # open < n
        # only add close ) if # close < # open
        # valid parent pairs IFF # open == # close == n
        if num_open == n and num_close == n:
            valid_parens.append("".join(stack))
            return
        
        if num_close < num_open:
            stack.append(")")
            backtrack(num_open, num_close + 1)
            stack.pop() # backtrack (undo) the operation to try other scenarios (i.e., append '(' )

        if num_open < n:
            stack.append("(")
            backtrack(num_open + 1, num_close)
            stack.pop() # # backtrack (undo) the operation to try other scenarios (i.e., append ')')

    backtrack(num_open=0, num_close=0)

    return valid_parens


def generateParenthesis(n: int) -> List[str]:
    """
    time complexity:
    space complexity:
    """
    
    # stores all valid pairs once found
    valid_parens = []

    # used to build the parentheses pairs
    #stack = []

    def backtrack(num_open, num_close, p_pair):

        # only add open ( if # open < n
        # only add close ) if # close < # open
        # valid parent pairs IFF # open == # close == n
        if num_open == n and num_close == n:
            valid_parens.append("".join(p_pair))
            return
        
        if num_close < num_open:
            p_pair.append(")")
            backtrack(num_open, num_close + 1, p_pair)
            
            # NOTE: we need to pop because we have a GLOBAL stack; in the `test` function, 
            #       we're building a new pair every recursive call (not global)
            p_pair.pop() # backtrack (undo) the operation to try other scenarios (i.e., append '(' )

        if num_open < n:
            p_pair.append("(")
            backtrack(num_open + 1, num_close, p_pair)
            p_pair.pop() # # backtrack (undo) the operation to try other scenarios (i.e., append ')')

    # impossible to start with ")" for valid parentheses
    backtrack(num_open=1, num_close=0, p_pair=["("]) 

    # NOTE: passing in this list is still global stack even though we pass it around in the function,
    #       we just have to because i did not set this to a variable; the better solution is making a global
    #       stack variable and not passing it around in the recursive call or just use the `test` solution

    return valid_parens


def test(n: int) -> List[str]:
    """
    time complexity:
    space complexity:
    """
    
    # stores all valid pairs once found
    valid_parens = []

    # used to build the parentheses pairs
    #stack = []

    def backtrack(num_open, num_close, p_pair):

        # only add open ( if # open < n
        # only add close ) if # close < # open
        # valid parent pairs IFF # open == # close == n
        if num_open == n and num_close == n:
            valid_parens.append(p_pair)
            return
        

        if num_open < n:
            backtrack(num_open + 1, num_close, p_pair + "(")
            #p_pair.pop() # # backtrack (undo) the operation to try other scenarios (i.e., append ')')

        if num_close < num_open:

            backtrack(num_open, num_close + 1, p_pair + ")")
            #p_pair.pop() # backtrack (undo) the operation to try other scenarios (i.e., append '(' )



    # impossible to start with ")" for valid parentheses
    backtrack(num_open=0, num_close=0, p_pair="")

    return valid_parens



if __name__ == "__main__":

    # test cases

    case_1 = 3

    ret = generateParenthesis(case_1)

    print(ret)

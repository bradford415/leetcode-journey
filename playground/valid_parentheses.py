
matches = {")": "("}


def is_valid(p_pair):

    stack = []

    for char in p_pair:
        
        if char in matches.values():
            # add paren to stack if it's open
            stack.append(char)
        else:
            # if closed, find if the top of stack is open
            if stack:
                stack_char = stack.pop()
                if matches[char] != stack_char:
                    return False
            else:
                # invalid permuation, remove from list
                return False
    if stack:
        return False
    return True

input_str = "()()()"
input_str_2 = "()()("
input_str_3 = "()()())"

print(is_valid(input_str_3))
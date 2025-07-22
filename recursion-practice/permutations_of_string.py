

result = []

def find_permutations(index, permutation):

    #base_case: if 'index' has reached the end of the string we have a complete permutation
    if index == len(permutation):
        result.append("".join(permutation))
        return
    
    # fix the char at the current index and swap with all other possible indices and recurse;
    # NOTE: setting the loop to start at `index` fixes the char before `index` and only swaps the remaining
    #       indices that are unfixed, this prevents unnecessary work and duplicate combination 
    # For example: if `index=0` (nothing is fixed) then ABC -> swap A with A = ABC, then swap A with B = BAC, then swap A with C = CAB
    #              but if A is fixed `index=1` then swap A with B = BAC, then swap A with C = CAB
    for i in range(index, len(permutation)):
        # swap `index` and `i`
        # index represents the possible indices to swap (A, B, C) and i represents the current index (A)
        permutation[index], permutation[i] = permutation[i], permutation[index]
        
        # now that we've swapped the first `index` A,  we increment index to swap the remaining possiblities B & C (index+1)
        find_permutations(index+1, permutation)

        # backtrack (undo the swap) so we can try other paths 
        permutation[index], permutation[i] = permutation[i], permutation[index]


string = "ABC"
s_as_list = list(string) # convert to list bc strings are not mutable

find_permutations(0, s_as_list)

print(result)


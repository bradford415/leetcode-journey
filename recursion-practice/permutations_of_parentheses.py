

permutations = []

def permute(index, s):

    if index == len(s):
        permutations.append("".join(s))
        return
    
    # fix each position before `i`
    for i in range(index, len(s)):

        s[i], s[index] = s[index], s[i]
        permute(index + 1, s)
        s[i], s[index] = s[index], s[i]


input = "()" * 2

permute(0, list(input))

print(permutations)
print(f"number of permutations {len(permutations)}")

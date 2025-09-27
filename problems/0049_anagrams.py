from typing import List, Optional
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    time complexity: O(m * n)
        - m to loop through the whole array
        - n is the average length of the strings because we have to loop 
          through each character to make a count dictionary
    space complexity:
    """

    anagrams = defaultdict(list)
    for word in strs:
        key = [0] * 26
        for char in word:
            key[ord(char) - ord("a")] += 1
        
        anagrams[tuple(key)].append(word)
    
    return list(anagrams.values())


if __name__ == "__main__":

    # test cases
    case_1 = ["eat","tea","tan","ate","nat","bat"]

    ret = groupAnagrams(case_1)
    print(ret)

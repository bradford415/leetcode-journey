from typing import Optional


def lengthOfLongestSubstring_brute(s: str) -> int:
    """
    time complexity: O(n^3)
        - iterating through the string in a nested loop
        - the `in` operator worst case will have the same length as s
    space complexity: O(n)
        - worst case the substring length equals len(s)
    """

    longest_ss = ""

    # loop through each character in s and start building the substring
    for i in range(len(s)):
        substring = ""
        substring += s[i]

        # iterate through the rest of the string until a duplicate is found and break
        for j in range(i+1, len(s)):
            if s[j] not in substring:
                substring += s[j]
            else:
                break

        # after a duplicate is found or the end of the string is reached, check if the substring
        # is longer than the longeset one
        if len(substring) > len(longest_ss):
            longest_ss = substring
    
    return len(longest_ss)

def lengthOfLongestSubstring(s: str) -> int:
    """
    time complexity: O(n)
        - right pointer moves at most n times and left pointer moves at most n times
        - set `in` is O(1) NOTE: we usually measure time complexity in worst case so `in` set worst case is O(n)
                                 but this is incredibly rare so we say it's O(1); similar to why we say quicksort
                                 is O(nlogn)
    space complexity: O(k) or O(n)
        - where k is the character set; since there's not duplicate characters, if the problem is limited to 
          lower case characters there can only be maximum 26 characters in the set which is constant 
          (or 128 if limited to standard ASCII)
        - if the the problem is any Unicode character then the space complexity is O(n) since Unicode is 
          much larger, n = length of string
    """

    longest_ss = 0

    # use a set as the substring for instanenous lookups O(1)
    substring = set() # cannot create an empty set in python with {} (it creates a dict)
    
    # use left and right pointers to act as the sliding window
    left = 0
    for right in range(len(s)):

        # if the current char (right) is in the substring, we need to remove it from the left
        # side, update the left pointer, and then add it to the substring; the duplicate character
        # won't always be on the edge of the substring, so we need the while loop move the left
        # pointer until it's no longer in the list
        while s[right] in substring:
            substring.remove(s[left])
            left += 1

        substring.add(s[right])
        
        if len(substring) > longest_ss:
            longest_ss = len(substring)
    
    return longest_ss




if __name__ == "__main__":
    
    s = "abcabcbb"

    ret = lengthOfLongestSubstring_brute(s)
    
    print(ret)

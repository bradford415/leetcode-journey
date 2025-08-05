from typing import List, Optional


def findSubstring(self, s: str, words: List[str]) -> List[int]:
    """
    NOTE: This is the closest I've gotten, passes 181/182 test cases but runs out of time on the last one
          TODO: comeback to this and fix it
    time complexity:
    space complexity:
    """
    win_len = len(words[0])
    num_words = len(words)
    perm_len = win_len * num_words

    freq_map = self.create_freq_map(words)

    ret_inds = []

    for i in range(len(s) - perm_len + 1):

        # check each word to see if it matches
        failed_check = 0
        for j in range(num_words):
            sub_s = s[j*win_len + i: (j+1)*win_len + i]

            if sub_s in freq_map:
                if freq_map[sub_s] > 0:
                    freq_map[sub_s] -= 1
                    #break
                else:
                    failed_check = 1
                    break
            else:
                failed_check = 1
                break

            if failed_check:
                break

        if not failed_check:
            ret_inds.append(i)

        # reset frequency map once we know a start index is invalid
        freq_map = self.create_freq_map(words)

    return ret_inds

def create_freq_map(self, words):
    freq_map = {}
    for w in words:
        if w in freq_map:
            freq_map[w] += 1
        else:
            freq_map[w] = 1

    return freq_map


if __name__ == "__main__":

    # test cases

    ret = functionName()
    print(ret)

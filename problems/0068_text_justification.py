from typing import List, Optional

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """TODO: unfinished, need to work out some edge cases if it's even worth finishing

        time complexity:
        space complexity:
        """
        
        result = []

        line_words = []
        max_word_len = 0
        for word_i in range(len(words)):
            # gather the indices of the words to use for the line
            if max_word_len + len(words[word_i]) <= maxWidth - len(line_words) - 1:
                max_word_len += len(words[word_i])
                line_words.append(word_i)
                continue

            spaces_needed = maxWidth - max_word_len
            num_gaps = len(line_words) - 1 if len(line_words) > 1 else 1

            if spaces_needed % num_gaps == 0:
                spaces_gap = [spaces_needed // num_gaps] * num_gaps
            else:
                spaces_per_gap =  spaces_needed // 2
                spaces_gap =  [spaces_needed - spaces_needed * (num_gaps - 1)] +  [spaces_per_gap] * (num_gaps - 1)
        
            just_line= ""
            for ind in range(len(line_words)):
                if ind < len(spaces_gap):
                    just_line += words[line_words[ind]] + " " * spaces_gap[ind]
                else:
                    just_line += words[line_words[ind]]


            line_words = [word_i]
            
            result.append(just_line)

        return result



if __name__ == "__main__":

    # test cases
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    
    solution = Solution()

    ret = solution.fullJustify(words, maxWidth)
    print(ret)

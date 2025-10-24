from typing import List, Optional

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        time complexity:
        space complexity:
        """

        perm = ""
        k -= 1

        factorial = 1
        sequence = []
        for i in range(1, n):
            factorial *= i 
            sequence.append(i)
        sequence.append(n)

        while True:
            perm += str(sequence[k // factorial])
            del sequence[k // factorial]

            if not sequence:
                break

            k %= factorial
            factorial //= len(sequence)

        return perm



if __name__ == "__main__":

    # test cases
    case_1 = 4
    
    solution = Solution()

    ret = solution.getPermutation(case_1, 3)
    print(ret)

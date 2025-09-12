from typing import List, Optional

class Solver:

    def jump_recursive(self, nums: List[int]) -> int:
        """My own attempt of a recursive solution and added memoization for DP but time limit exceeded
        It passed a lot of cases so I think the logic is correct just too expensive

        I think correct DP approach is O(n^2) - TODO understand the dp approach


        time complexity:
        space complexity:
        """
        self.min_jumps = len(nums)
        

        memo = {}

        def bfs(cur_idx, n, curr_jumps):

            if cur_idx in memo:
                cur_idx  = memo[(cur_idx, n, curr_jumps)]

            if cur_idx == n - 1:
                if self.min_jumps > curr_jumps:
                    self.min_jumps = curr_jumps
                    memo[(cur_idx, n, curr_jumps)] = self.min_jumps
                return
            if cur_idx > n - 1:
                return

            num_jumps = nums[cur_idx]
            for i in range(1, num_jumps+1):
                
                bfs(cur_idx + i, n, curr_jumps + 1)

        bfs(0, len(nums), 0)

        return self.min_jumps
    

    def jump_greedy(self, nums: List[int]) -> int:
        """       
        time complexity: O(n)
        space complexity:
        """
        
        result = 0
        left = 0
        right = 0

        while right < len(nums) - 1:

            # find the farthest location in the group we can jump
            farthest = 0
            for i in range(left, right + 1): # +1 to make right inclusive
                farthest = max(farthest, i + nums[i])

            # update the left and right pointers for the next group
            left = right + 1
            right = farthest

            # the number of groups will be the min number of jumps
            result += 1
        
        return result



if __name__ == "__main__":

    # test cases
    nums = [2,3,0,1,4]

    solve = Solver()

    #ret = solve.jump_recursive(nums)
    ret = solve.jump_greedy(nums)
    print(ret)

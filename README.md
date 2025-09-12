# leetcode-journey
Code and notes repository for my leetcode journey

## Study plan
1. Study data structures part 1
   - Arrays
     - [array problems](https://leetcode.com/problem-list/array/)
   - Linked lists
     - [linked list problems](https://leetcode.com/problem-list/linked-list/)
   - Maps
     - [hash table problems](https://leetcode.com/problem-list/hash-table/)
   - Know the time complexity and space complexity of each
   - Do three problems for each category
2. Study data structures part 2
   - Searching algorithms
     - binary search
       - [binary search problems](https://leetcode.com/problem-list/binary-search/)
     - linear search
   - Sorting algorithms
     - quicksort
   - Trees
     - pre, in, and post traversals for binary trees
     - [binary tree problems](https://leetcode.com/problem-list/binary-tree/)
     - [binary search tree problems](https://leetcode.com/problem-list/binary-search-tree/)
   - Know the time complexity and space complexity of each
   - Do a few problems for each category
3. Do the first 1-50 problems in order

### Other sets of problems to do
- Blind 75
  - The 75 problems are specifically chosen because they cover the most fundamental and frequently asked data structures and algorithmic patterns in technical coding interviews for software engineering roles
- Neet Code 150

## Interview Tips
Treat LeetCode like an interview

### Before writing code for a problem
- Ensure you fully understand the problem
- Ask clarifying questions

### Notes:
- Do NOT spend longer than 40 minutes on a problem (start a timer when I start the problem)

## Resources
__Algorithms__
- Sorting
  - [merge sort](https://www.youtube.com/watch?v=3j0SWDX4AtU&ab_channel=BroCode)
- Super easy to understand tree traversals for [preorder](https://www.youtube.com/watch?v=1WxLM2hwL-U&ab_channel=MichaelSambol), [inorder](https://www.youtube.com/watch?v=5dySuyZf9Qg&ab_channel=MichaelSambol), and [postorder](https://www.youtube.com/watch?v=4zVdfkpcT6U&ab_channel=MichaelSambol)

__Official Interview Guides__
  - [Meta's official interview guide](https://www.metacareers.com/swe-prep-onsite)
    - note it mentions that Meta does NOT ask Dynamic Programming (DP) problems
   

## Concepts that you should be able to code by muscle memory
* Binary search
* DFS (pre, in, post)
* Permutation of a string recursively

## Problems completed:
| Problem # | Name                                 | Help Hint                                                                                    |
|-----------|--------------------------------------|----------------------------------------------------------------------------------------------|
| 1         |  Two Sum                             | hash map and subtract target - value                                                         |
| 2         |  Add Two Numbers                     | iterate both linked lists and perform handwritten addition normally                          |
| 3         |  Longest substring No Repeat Chars   | sliding window w/ left & right pointer, use set for substring                                |
| 5         |  Longest Palindromic Substring       | loop all chars, use L/R pointers expanding outwards, even & odd substrings in 2 while loops  |
| 6         |  Zigag Conversion                    | increment to get to next char, for middle rows handle the extra character                    |
| 7         |  Reverse Integer                     | result = result*10 + integer % 10, reduce number -> int(x / 10); check overflow on last digit|
| 10        |  Regular Expression Matching         | TODO: need to go back and look through this problem and finish it                            |
| 11        |  Container With Most Water           | left and right pointers at opposite ends of array                                            |
| 12        |  Integer to Roman                    | build Roman numeral map and include the "special cases"                                      |
| 13        |  Roman to Integer                    | build map and include special cases or subtract the symbol if it's smaller than the next     |
| 15        |  Three Sum                           | sort array, fix a number and make two sum problem then use L & R pointers                    |
| 17        |  Letter Combos of a Phone Number     | Backtrack with recursion                                                                     |
| 19        |  Remove Nth Node From End of List    | count elements                                                                               |
| 20        |  Valid Parentheses                   | add to stack until closing brace, use map for open-close pair, pop stack pair matches        |
| 21        |  Merge Two Sorted Lists              | loop till end of 1 list, link smaller val, link remaining list                               |
| 22        |  Generate Parentheses                | backtrack; base case: # open == # close == n, add '(' if < n, add ')' if # close < # open    |
| 23        |  Merge k Sorted Lists                | merge 2 lists at a time ("divide & conquer"), repeating until there's only 1 list left       |
| 24        |  Swap Nodes in Pairs                 | loop each pair while a pair exists, use ptrs & dummy node to swap pairs nodes one at a time  |
| 25        |  Reverse Nodes in k-Group            | find kth node ptr, reverse linked list with kth.next, link groups stop when kth node == null |
| 26        |  Remove Duplicates from Sorted Array | save highest unique & next idx, loop through array, if curr val > highest unique then swap   |
| 27        |  Remove Element                      | k=0, loop through array (i), if arr[i] == val, swap k and i, increment k, return k           |
| 30        |  Substring Concatentation All Words  | sliding win + map; create freq_map, decrement map if sub_s in map, invalid if freq <= 0      |
| 31        |  Next Permutation                    | find break point, swap with num <= bp+1 and num > bp, reverse elements right of bp (see code)|
| 33        |  Search in Rotated Array             | bin search, determine if M is in left or right sorted portion, adjust L/R based on target    |
| 34        |  First & Last Position Sorted Array  | double modified bin search, one for L index and one for R index; modified=continue search    |
| 35        |  Search Insert Position              | binary search, return L if not found in array                                                |
| 35        |  Search Insert Position              | binary search, return L if not found in array                                                |
| 38        |  Count and Say                       | iterative sliding window                                                                     |
| 39        |  Combination Sum                     | recursive decision tree where right subtree cannot include last element of left subtree      |
| 40        |  Combination Sum 2                   | sort candidates, recursive decision tree like LC 39, right subtree skip duplicates           |
| 41        |  First Missing Positive              | modify input; 1st set negs to 0, 2nd set pos ints inds to negs, 3rd if val inds neg val exist|
| 42        |  Trapping Rain Water                 | L/R pointers; shift L or R if min(max_L, max_R), calc rain min(max_L, max_R) - height[curr]  |
| 43        |  Multiply Strings                    | Convert str to int (ascii to int, multiply by 10 by position and sum), mult, int back to str |
| 44        |  Wildcard Matching                   | recursive exhaustion, matching regularly, and branch recursion on "*"; dp (memoization)      |
| 45        |  Jump Game 2                         | L/R, num_groups = min_jumps O(n); or DP O(n^2) TODO still need to understand DP approach     |
| 96        |  Valid Sudoku                        | double for loop to validate rows, cols, squares with map of sets; squares use tuple as keys  |
| 98        |  Validate Binary Search Tree         | validate node.val w/ bounds; move left -> update right bound, move right -> update left bound|
| 98        |  Validate Binary Search Tree         | inorder traversal then check if list is sorted                                               |
| 99        |  Recover Binary Search Tree          | inorder traversal, swap first & last violation or swap first & middle violation if adjacent  |
| 206       |  Reverse Linked List                 | while curr, set ptr to last_node.next, set|

## Quick formulas
| Description                                        | Formula         |
|----------------------------------------------------|-----------------|
| Number of permutations in a string (distinct chars) | n!             |


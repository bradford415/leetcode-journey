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

## Notes:
- Do NOT spend longer than 40 minutes on a problem (start a timer when I start the problem)

## Resources
- Super easy to understand tree traversals for [preorder](https://www.youtube.com/watch?v=1WxLM2hwL-U&ab_channel=MichaelSambol), [inorder](https://www.youtube.com/watch?v=5dySuyZf9Qg&ab_channel=MichaelSambol), and [postorder](https://www.youtube.com/watch?v=4zVdfkpcT6U&ab_channel=MichaelSambol)

## Problems completed:
| Problem # | Name                                | Help Hint                                                                                   |
|-----------|-------------------------------------|---------------------------------------------------------------------------------------------|
| 1         |  Two Sum                            | hash map and subtract target - value                                                        |
| 2         |  Add Two Numbers                    | iterate both linked lists and perform handwritten addition normally                         |
| 3         |  Longest substring No Repeat Chars  | sliding window w/ left & right pointer, use set for substring                               |
| 11        |  Container With Most Water          | left and right pointers at opposite ends of array                                           |
| 12        |  Integer to Roman                   | build Roman numeral map and include the "special cases"                                     |
| 13        |  Roman to Integer                   | build map and include special cases or subtract the symbol if it's smaller than the next    |
| 15        |  Three Sum                          | sort array, fix a number and make two sum problem then use L & R pointers                   |
| 17        |  Letter Combos of a Phone Number    | Backtrack with recursion                                                                    |
| 19        |  Remove Nth Node From End of List   | count elements                                                                              |
| 21        |  Merge Two Sorted Lists             | loop till end of 1 list, link smaller val, link remaining list                              |
| 33        |  Search in Rotated Array            | bin search, determine if M is in left or right sorted portion, adjust L/R based on target   |
| 34        |  First & Last Position Sorted Array | double modified bin search, one for L index and one for R index; modified=continue search   |
| 96        |  Unique Binary Search Trees         | DP; consider every node to be root, find number of tree combinations in L & R subtrees      |


'''
1. Generate All Subsets of a Set

Problem: Given a set of distinct integers, return all possible subsets (the power set).
Example Input: [1, 2, 3]
Example Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]


Restate:
Given a set of distinct integers return all possible unique subsets

Algorithm Backtracking

Steps:
1. Each element in the array can either be included or excluded in a subset
2. Use recursion to explore both choices for every element

Pseudo code:
- initialize result
- create backtrack method passing in index, current_subset --> index is the state, current_subset is the option
    - base case
        - add the current_subset to the result
        - if index == len(nums): append current_subset to the result and return

    - options block
        - append current element to current_subset
        - recurse by calling backtrack with params index + 1 and current_subset
        - remove the current element with current_subset.pop()
        - recurse backtrack again with params index + 1 and current_subset
- Call backtrack to start the process with params 0 and empty list
- return result
'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Restate: Given distinct integers, return all unique subsets.

        Algorithm: Backtracking
        Steps:
        - base case index == len(nums) --> add to result array --> return
        - options case
            add index value  --> to subset
            recurse with index + 1 and subset
            pop it out
            recurse with index + 1 and subset
        call backtrack
        return result

        Time Complexity: O(K^N)
        space complexity: O(N)
        '''

        result = []
        def backtrack(index: int, current_subset: list) -> list[list]:
            if index == len(nums):
                result.append(list(current_subset))
                return

            current_subset.append(nums[index])
            backtrack(index+1, current_subset)

            current_subset.pop()
            backtrack(index+1, current_subset)

        backtrack(0, [])
        return result

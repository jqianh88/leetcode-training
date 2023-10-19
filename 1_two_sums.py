"""
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return 
the answer in any order.

Inputs: 
 - nums: array of integers 
 - target: an integer 

Outputs: 
 - array of indices. 
"""

""" First Pass 10/1/23"""
# def two_sums(nums: list, target: int) -> list: 
#     hashmap = {}
#     for i, num in enumerate(nums):
#         hashmap[num] = i

#     for num in hashmap: 
#         second_num = target - num

#         if second_num in hashmap:
#             return [hashmap[num], hashmap[second_num]]


"""Second Pass 10/12/23"""
#Runtime: Beats 52.21%of users with Python
# Memory: 77.95%of users with Python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            potential_solution = target-num
            if potential_solution in nums and nums.index(potential_solution) != i: 
                return [i, nums.index(potential_solution)]


if __name__ == '__main__':
    target = 5
    nums = [1, 2, 4, 3]
    self = Solution()
    desired_target = self.twoSum(nums=nums, target=target)
    # desired_target = two_sums(nums=nums, target=target)
    print(desired_target)


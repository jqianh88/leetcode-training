
from math import prod
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ### Not a valid solution because not allowed 
        #### to use copy() or prod()
        ### alternative has to large of a time complexity
        # hash_nums = {}
        # for i, num in enumerate(nums):
        #     temp_nums = nums.copy()
        #     temp_nums.pop(i)
        #     index_sum = prod(temp_nums)
        #     hash_nums[num] = index_sum

        # return list(hash_nums.values())
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



if __name__=="__main__":
    self = Solution()
    nums = [-1,1,0,-3,3]
    print(self.productExceptSelf(nums))
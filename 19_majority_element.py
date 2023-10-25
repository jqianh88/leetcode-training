import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_value = 0
        majority_key = 0
        for key, value in collections.Counter(nums).items():

            if value > len(nums)//2 and value > majority_value: 
                majority_value = value
                majority_key = key

        return majority_key
    


if __name__=='__main__':
    self = Solution()
    nums = [2,2,1,1,1,2,2]
    print(self.majorityElement(nums=nums))
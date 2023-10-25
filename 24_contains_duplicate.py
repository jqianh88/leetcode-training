class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) == len(nums):
            return False 
        return True
    


if __name__=='__main__':
    self = Solution()
    nums = [1, 2, 2, 3, 4]
    print(self.containsDuplicate(nums=nums))
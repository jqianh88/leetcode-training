'''
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. 
If `target` exists, then return its index. Otherwise, return `-1`. 

You must write an algorithm with O(log n) runtime complexity. 
Inputs: 
- nums: list
- target: int

Outputs: 
- index: int ortherwise -1
'''

def binary_search(nums: list, target: int) -> bool:

    hashmap = {num: i for i, num in enumerate(nums)}
    if target in hashmap: 
        return hashmap[target]

    return -1






if __name__=='__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(nums=nums, target=target))
"""
Given a string `s` containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. 

An input string is valid if: 
1. Open brackets must be closed by the same type of brackets. 
2. Open brackets must be closed in the correct order. 
3. Every close bracket has a corresponding open bracket of the same type.

Inputs: 
 - s: string with only the characters '(', ')', '{', '}', '[', and ']'

Outputs: 
 - boolean
"""

#This version doesn't work fully
# def valid_parentheses(s: str) -> bool: 
#     valid_hashmap = {'(': ')', '{': '}', '[': ']'}

#     string_hashmap = {i: p for i, p in enumerate(s)}

#     # Check length 
#     if len(s) % 2 != 0:
#         return False
    
#     even_nums = [i for i in range(len(s)) if i % 2==0]
#     for num in even_nums:
#         if not (s[num] in valid_hashmap and s[num+1]==valid_hashmap[s[num]]):
#             return False
#     return True


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        character_map = {'(':')', '{':'}','[':']'}
        stack = []
        for el in s: # loop through each character in the string 
            if el in character_map: # 1
                stack.append(el)
            elif len(stack) == 0 or character_map[stack.pop()] != el: # 2
                return False 
        return len(stack) == 0 # 3


'''
# Another Version
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] # create an empty stack to store opening brackets 
        for c in s: # loop through each character in the string 
            if c in '([{':
                stack.append(c)
            else: 
                if not stack or (c==')') and stack[-1] != '(' or (c==']') and stack[-1] != '[' or (c=='}') and stack[-1] != '{':
                    return False 
                stack.pop()
        return not stack
'''


    
    




if __name__ == '__main__':

    s = '()[][]'
    self = Solution()
    print(self.isValid(s))

    
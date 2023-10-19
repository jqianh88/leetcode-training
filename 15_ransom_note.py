class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # iterate magazine and pop ransom note with the index of the char.
        # if ransom note empty at the end return true otherwise false
        rn_list = [c for c in ransomNote]
        for char in magazine: 
            if char in rn_list: 
                rn_list.pop(rn_list.index(char))
        if len(rn_list) == 0:
            return True 
        return False
    

if __name__=='__main__':
    self = Solution()
    ransomNote = 'aa'
    magazine = 'aab'
    print(self.canConstruct(ransomNote=ransomNote, magazine=magazine))
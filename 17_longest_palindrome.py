import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 
        for i in collections.Counter(s).values():
            res += i // 2 *2 
        return min(res+1, len(s))
    


if __name__=='__main__':
    self = Solution()
    s = 'ccc'
    print(self.longestPalindrome(s=s))
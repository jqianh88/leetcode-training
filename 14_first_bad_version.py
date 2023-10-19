# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

'''
You are a product manager and currently leading a team to develop a 
new product. Unfortunately, the latest version of your product fails 
the quality check. Since each version is developed based on the 
previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out 
the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether 
version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

'''

def isBadVersion(version):
    if version in [1, 2, 3]:
        return False

    return True
class Solution(object):
    def firstBadVersion(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        left = 1
        right = n
        while left < right: 
            mid = left + (right-left) // 2
            if isBadVersion(mid):
                right = mid 
            else: 
                left = mid + 1
        return left 


if __name__=='__main__':
    self = Solution()
    n = 5
    print(self.firstBadVersion(n))



'''
Approach
In this solution, we maintain two pointers left and
 right that represent the range of versions we are searching.
 We start with left = 1 and right = n. At each iteration of 
 the while loop, we compute the midpoint mid of the range as
   (left + right) // 2, and we call the isBadVersion API to 
   check whether version mid is bad or not.

If isBadVersion(mid) returns True, then we know that the first bad 
version must be in the range [left, mid], so we update right = mid. 
Otherwise, the first bad version must be in the range [mid+1, right],
 so we update left = mid + 1. We continue this process until left 
 and right converge to a single version, which must be the first
   bad version.

This algorithm runs in logarithmic time and makes only O(1) 
calls to the isBadVersion API at each iteration, which minimizes
 the total number of calls to the API.


'''

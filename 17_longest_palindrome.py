import collections



    # Own thought process of doing it - Not as efficient but doesn't use any imports
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     response = 0 
    #     count_hashmap = {letter: s.count(letter) for letter in s}

    #     for num in list(count_hashmap.values()):
    #         response += num // 2 * 2
    #     return min(response+1, len(s))

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        response = 0 
        for i in collections.Counter(s).values():
            response += i // 2 *2 
        return min(response+1, len(s))



    


if __name__=='__main__':
    self = Solution()
    s = 'ccc'
    print(self.longestPalindrome(s=s))


    '''
    collection: 
    This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.

    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * ChainMap     dict-like class for creating a single view of multiple mappings
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values
    * UserDict     wrapper around dictionary objects for easier dict subclassing
    * UserList     wrapper around list objects for easier list subclassing
    * UserString   wrapper around string objects for easier string subclassing
    '''
'''
Big O Notation

Describes the run time complexity of your algorithm as your input size increases. 
- Not we don't care about constant values like n/2 or n + 5 it will round to n
- We always care about the worst case run time

The most common Big O run times in ascending order are 
- O(1): flat line (constant)
    - Examples
        - Array 
            - push to end (append)
            - pop from the end (pop)
            - lookup (nums[0])
        - Hashmap / Set
            - Insert (hashmap["key"] = 10)
            - Lookup ("key" in hashmap or hashmap["key"])
            - Remove (hashmap.pop("key"))

- O(logn): way more efficient than O(n) 
    --> How many times can you divide by 2 until you get to 1
    how many times can you multiply 1 by 2 to get n --> 2^x = n
    log2^x - logn --> x = log_2(n)

    - Binary Search on BST: if you have a balanced Binary search tree
        - Because you go to the left when looking for some target value
        which divides by 2 each time --> do this recursively
        
        def search(root, target): 
            if not root: 
                return False 
            if target < root.val:
                return search(root.left, target)
            elif target > root.val: 
                return search(root.right, target) 
            else: 
                return True
                
    - Heap Push and Pop
        import heapq 
        minHeap = []
        heapq.heappush(minHeap,5)
        heapq.heappop(minHeap)
- O(sqrt(n))
    - More of a math problem: Find all factors of a given number n. 
    So you only need to look in the range of the square root of n + 1

    import math 
    n = 12 
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1): 
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    print(factors)


- O(n): linear time (y = x) ---- As input size grows time grows 
    - Array
        - Sum of array (sum(nums))
        - loops (for n in nums)
        - Inserting in the middle of the array, because after you insert
        you have to move the remaining numbers to the right 
            - nums.insert(1, 100)
        - Removing in the middle of the array, because you remove an then 
        move the remaining numbers to the left
            - nums.remove(100)
        - Searching in the middle of the array: have to look through entire 
        array to find whether the number exists or not
            - print(100 in nums)
        - Building heap: more efficient to build it from scratch like this (O(n) time)
            - heapq.heapify(nums)
        - Sliding windows algorithm
            - It does have nested loops but it doesn't mean that the 
                time complexity is n^2
        - Monotonic stack algorithm: also only O(n)

- O(nlogn) 
    - HeapSort: 

    import heapq 
    nums = [1, 2, 3, 4,5]
    heapq=heapify(nums) # O(n)
    while nums: 
        heapq.heappop(nums) # (O(logn))
    --> In total it was actual n + nlogn run time but rounds to nlogn
    - MergeSort and most built in sort functions 

- O(n^2)
    - 2D array (list of lists): you need nested loops to traverse that
        - for i in range(len(nums)): # every row
            for j in range(len(nums[i])):  # every position
                print(nums[i][j])
    - Get every pair of elements in array 
        - iterate through a single array but iterate through it n times --> n^2
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(nums[i]. nums[j])
        --> The actualy time complexity comes down to the series 
            Summation (n^2/2) but for big O notation it n^2
    - Insertion Sort
        - insert in the middle n times -> n^2

- O(n*m)
    - Get every pair of elements from 2 arrays 
        nums1, nums2 = [], []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                print(nums1[i], nums2[j])

    - Traverse a rectangular grid 
        nums = [[1, 2, 3], [1, 2, 3]]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                print(nums[i][j])

- O(n^3) --> not efficient
    - Get every unique triplet of elements in array 
    nums = [1,2 ,3]
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)):
            for k in range(i+1, len(nums)):
                print(nums[i], nums[j], nums[k])

- O(2^n) --> not efficient
    - Recursion, tree height n, two branches
    Building 2 branches at the same time

    def recursion(i, nums): 
        if i == len(nums):
            return 0 
        branch1 = recursion(i+1, nums)
        branch2 = recursion(i+2, nums)

    Examples: Get all possible combinations, or the fibonacci sequence

- O(c^n)
    - Build n branches at the same time (c branches, where c is sometimes n)
    def recursion(i, nums, c): 
        if i == len(nums): 
            return 0 
        for j in range(i, i + c):
            branch = recursion(j+1, nums)
    

- O(n!): very rare that this comes up --> and super inefficient
    - Permutations 

    - Travelling salesman problem (Graph problem)
    '''
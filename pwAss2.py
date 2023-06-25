'''Answer 1
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = list(nums)
        n.sort()
        s = 0
        i = 0
        while i < len(n):
            s += n[i]
            i += 2
        return s

Answer 2

class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        l=list(candyType)
        s=set(candyType)
        s=list(s)
        s1=len(s)
        n=len(l)/2
        if n<=s1:
            return n
        else:
            return s1


Answer3

class Solution:
    def findLHS(self, nums):
        nums.sort()
        left = 0
        right = 1
        result = 0
        while right < len(nums):
            diff = nums[right] - nums[left]
            if diff == 1:
                result = max(result, right - left + 1)
            if diff <= 1:
                right += 1
            else:
                left += 1
        return result


Answer4

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):  # can place?
                n -= 1
                if n == 0: return True
                flowerbed[i] = 1  # palce!
        return False



Answer 5
# Approach 1
        
# class Solution:
#     def maximumProduct(self, nums):
#         nums.sort()
#         return max ( nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])


# Approach2

class Solution:
    def maximumProduct(self, nums):
        
        min1=1001
        min2=min1
        max1=-1001
        max2=max1
        max3=max2
        n=len(nums)
        for i in range(n):
            m=nums[i]

            # compare for 3 consecutive max
            if m>max1:
                max3=max2
                max2=max1
                max1=m
            elif m>max2:
                max3=max2
                max2=m
            elif m>max3:
                max3=m

            # compare for 2 min

            if m<min1:
                min2=min1
                min1=m
            elif m<min2:
                min2=m

        return max(min2*min1*max1,max1*max2*max3)

        
Answer 6
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

Answer 7

class Solution:
    def isMonotonic(self, A) :
        if A[-1] < A[0]: 
            A = A[::-1]
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True


Answer 8
class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi=max(nums)
        minnn=min(nums)
        return max(0,maxi-k-minnn-k)

        '''
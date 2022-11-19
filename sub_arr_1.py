class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        this is the faster solution
        
        sliding window
        
        iterate through the nums
        
        '''
        maxSum = nums[0]
        tempSum = 0
        
        for each in nums:
            
            # at any iteration if tempSum is a negative value, which means array up to that point could be ignored when looking for the max value, so tah
            # temp sum is set to 0
            
            if tempSum < 0:
                tempSum = 0
            tempSum += each
            
            maxSum = max(tempSum,maxSum)
            
        return maxSum
                
            
                
        

obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 = [-2,1,-3,4,-1]
nums2 = -1
print(obj.maxSubArray(nums2))
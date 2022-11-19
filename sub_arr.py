class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        this total solution works but it is not fast enough
        '''
        
        max = 0
        def run(num, max_sum):
            temp_sum = 0
            for e in num:
                temp_sum += e
                if temp_sum > max_sum:
                    max_sum = temp_sum
                
            print(temp_sum, max_sum)
            num.pop(0)
            if num:
                return run(num,max_sum)
            
            return max_sum
              
        # max = run(nums,0)   <-- if we give 0 as the initiate value of max_sum, there would be a problem if "nums" only contain negative values.
        # . -10 ^ 4 <= nums[i] <= 10 ^ 4
        # so that we need to give the lowest posible negative number to max sum. 
        #  float('-inf') <-- this returns the lowest posible negative value.
        
        max = run(nums,float('-inf'))
            
        return max  
            
        
            
        
        

obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 = [-2,1,-3,4,-1]
print(obj.maxSubArray(nums))
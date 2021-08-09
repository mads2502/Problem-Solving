class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_t=0
        max_s=nums[0]
        for i in nums:
            sum_t=sum_t+i
            if(sum_t>max_s):
                max_s=sum_t
            if(sum_t<0):
                sum_t=0
        return max_s
            

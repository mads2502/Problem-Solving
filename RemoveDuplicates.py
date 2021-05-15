import copy
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=sorted(list(set(nums)))
        for i in range(0,len(n)):
            nums[i]=n[i]
        return len(n)
            
        

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort=nums[0]
        hare=nums[0]
        while(1):
            tort=nums[tort]#1 unit jump
            hare=nums[nums[hare]] #2 unit jump
            if(tort==hare):
                break
        hare=nums[0]
        while(tort!=hare):
            hare=nums[hare]
            tort=nums[tort]
           
        return tort

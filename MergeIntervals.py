class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start=intervals[0][0]
        end=intervals[0][1]
        result=[]
        for i in intervals:
            if(i[0]<=end):
                end=max(i[1],end)
                start=min(start,i[0])
            else:
                result.append([start,end])
                start=i[0]
                end=i[1]
        result.append([start,end])
        return result
        
        

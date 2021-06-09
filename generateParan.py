class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans=[]
        self.generateparan(0,0,"",n)
        return self.ans
    def generateparan(self,l,r,curr,n):
        if len(curr)==2*n:
            self.ans.append(curr)#if length satisfies
            return
        if l<n:
            self.generateparan(l+1,r,curr+'(',n)
            if l>r:
                self.generateparan(l,r+1,curr+')',n)
        elif l>r:
            self.generateparan(l,r+1,curr+')',n)
        

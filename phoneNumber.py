class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.buttonmap={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        self.res=[]
        if digits=="":
            return []
        self.callme(digits,"",len(digits))
        return self.res
        
        
    def callme(self,digits,curr,l):
        if len(curr)==l:
            self.res.append(curr)
            return
        else:
            for i in range(len(digits)):
                for s in self.buttonmap[digits[i]]:
                    self.callme(digits[i+1:],curr+s,l)
            
        
                        
        

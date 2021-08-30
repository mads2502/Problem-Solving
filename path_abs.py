class Solution:
    def simplifyPath(self, path: str) -> str:
        l=path.split("/")
        stck=[]
        
        for i in l:
            if i=="..":
                if len(stck):
                    stck.pop()
                else:
                    continue
            elif i=="." or i=="":
                continue
            else:
                stck.append(i)
        print(l)
        return "/"+"/".join(stck)
        

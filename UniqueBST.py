# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        else:
            return self.subtreecombo(1,n)
    def subtreecombo(self,m,n):
        arr=[]
        if m>n:
            arr.append(None)
            return arr
        
        for i in range(m,n+1):
            left=self.subtreecombo(m,i-1)
            right=self.subtreecombo(i+1,n)#leaving alone the root node which is i    
            for val1 in left:
                for val2 in right:
                    myroot=TreeNode(i)
                    myroot.left=val1
                    myroot.right=val2
                    arr.append(myroot)
        return arr
        
                        
                
                
    
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        templist=[root]
        tlist=[]
        level=[]
        if root:
            res=[[root.val]]
        else:
            return
        while templist:
            for i in templist:
                if i.left:
                    level.append(i.left.val)
                    tlist.append(i.left)
                if i.right:
                    level.append(i.right.val)
                    tlist.append(i.right)
            templist=tlist
            tlist=[]
            if level:
                res.append(level)
            level=[]
        return res
                    
            
            
        
            
            
            
            
            
            
        

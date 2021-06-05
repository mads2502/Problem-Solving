# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root==None:
            return
        templist=[root]
        res=[]
        res.append(root.val/1.0)
        tlist=[]
        level=[]
        levelsum=0.0
        
        
        while templist:
            for i in templist:
                if i.left:
                    tlist.append(i.left)
                    levelsum+=i.left.val
                if i.right:
                    tlist.append(i.right)
                    levelsum+=i.right.val
            if  len(tlist):
                res.append(levelsum/len(tlist))
            
            templist=tlist
            tlist=[]
            levelsum=0.0
        return res
        

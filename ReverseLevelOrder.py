# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return
        templist=[root]
        tlist=[]
        res=[]
        level=[]
        while templist:
            for i in templist:
                if i.left:
                    level.append(i.left.val)
                    tlist.append(i.left)
                if i.right:
                    level.append(i.right.val)
                    tlist.append(i.right)
            if level:
                res.insert(0,level)
            level=[]
            templist=tlist
            tlist=[]
        res.append([root.val])
        return res

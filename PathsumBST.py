# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return
        else:
            return self.checksum(root,targetSum,0)
    def checksum(self,root,target,currsum):
        
        if not root:
            return 
        else:
            s=currsum+root.val
            if target==s and root.right==None and root.left==None:
                return True
        left=self.checksum(root.left,target,s) if root.left else False
        right=self.checksum(root.right,target,s) if root.right else False
        return  left or right
    
        

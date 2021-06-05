# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node,l,h):
            flag=False
            if node==None:
                return True
            if node:
                if node.val<h and node.val>l:
                    flag=True
                left=check(node.left,l,node.val)
                right=check(node.right,node.val,h)
            return flag and left and right
        return check(root,float('-inf'),float('inf'))
            
        
                
                
        

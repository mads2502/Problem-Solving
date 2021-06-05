# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root==None:
            return
        else:
            return self.mygranny(root,None,None)
    def mygranny(self,node,parent,gp):
        if node==None:
            return res
        res=0
        if node.left:
            left=self.mygranny(node.left,node,parent)
            res=res+left
        if node.right:
            right=self.mygranny(node.right,node,parent)
            res=res+right
        if gp and gp.val%2==0:
            res=res+node.val
        return res
    

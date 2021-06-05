# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left==None and root.right==None:
            return 1
        elif root.left==None:
            return 1+self.minDepth(root.right)
        elif root.right==None:
            return 1+self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.right),self.minDepth(root.left))

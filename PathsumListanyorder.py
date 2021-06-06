# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.cnt=0
        if not root:
            return 0
        else:
            self.count_of_paths(root,targetSum,[root.val])
            return self.cnt
    def count_of_paths(self,root,tsum,arr):
        if root:
            self.cnt+=arr.count(tsum)
            if root.left:
                self.count_of_paths(root.left,tsum,[i+root.left.val for i in arr]+[root.left.val])
            if root.right:
                self.count_of_paths(root.right,tsum,[i+root.right.val for i in arr]+[root.right.val])
        else:
            self.cnt=0
            
            
            

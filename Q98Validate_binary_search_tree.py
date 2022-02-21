# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(lower, upper, root):
            if not root:
                return True
            if root.val >= upper or root.val <= lower:
                return False
            return (helper(lower, root.val, root.left) and helper(root.val, upper,                           root.right))
        return helper(float('-inf'), float('inf'), root)

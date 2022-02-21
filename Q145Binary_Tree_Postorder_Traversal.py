# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(self, root, result):
            if root is not None:
                helper(self, root.left, result)
                helper(self, root.right, result)
                result.append(root.val)
        helper(self, root, result)
        return result

        

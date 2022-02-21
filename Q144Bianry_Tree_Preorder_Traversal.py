# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(self, root, result):
            if root is not None:
                result.append(root.val)
                helper(self, root.left, result)
                helper(self, root.right, result)
        helper(self, root, result)
        return result
        
        
        

            
        

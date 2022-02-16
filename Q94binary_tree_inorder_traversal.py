Given the root of a binary tree, return the inorder traversal of its
nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # defining the helper function that will be used for tree traversal
        def root_travel(root):
            # defining the exit base condition
            if not root:
                return
            root_travel(root.left)
            result.append(root.val)
            root_travel(root.right)
         
        root_travel(root)
        return result


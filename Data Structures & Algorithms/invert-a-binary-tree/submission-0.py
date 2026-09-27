# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            recurse(node.left)
            recurse(node.right)

            node.left, node.right = node.right, node.left
        
        recurse(root)
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return depth
            
            left = recurse(node.left, depth + 1)
            right = recurse(node.right, depth + 1)

            if abs(right - left) > 1:
                return float('inf')

            return max(left, right)
        
        return recurse(root, 0) != float('inf')
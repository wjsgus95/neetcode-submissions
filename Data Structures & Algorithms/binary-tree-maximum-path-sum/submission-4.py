# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def recurse(node: Optional[TreeNode]) -> int:
            nonlocal ans 

            if not node:
                return 0

            left = recurse(node.left)
            right = recurse(node.right)

            mid = max(left, right, 0) + node.val
            ans = max(ans, mid)
            ans = max(ans, left + node.val + right)

            return mid
        
        recurse(root)
        return ans
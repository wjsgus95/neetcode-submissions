# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        table = dict()

        def recurse(node: Optional[TreeNode]) -> int:
            nonlocal ans 

            if not node:
                return 0

            if not node.left and not node.right:
                table[node] = node.val
            
            left = recurse(node.left)
            right = recurse(node.right)

            table[node] = max(left, right, 0) + node.val
            ans = max(ans, table[node])
            if node.left and node.right:
                ans = max(ans, table[node.left] + node.val + table[node.right])

            return table[node]
        
        recurse(root)
        return ans
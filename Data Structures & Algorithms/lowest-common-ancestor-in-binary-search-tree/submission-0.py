# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return
            
            min_val, max_val = min(p.val, q.val), max(p.val, q.val)

            if node.val < min_val:
                return recurse(node.right)
            elif node.val > max_val:
                return recurse(node.left)
            else:
                return node
            
        return recurse(root)

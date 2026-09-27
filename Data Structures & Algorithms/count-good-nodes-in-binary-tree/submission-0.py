# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def recurse(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            new_max_val = max(node.val, max_val) 
            c = 1 if node.val >= max_val else 0

            return c + recurse(node.left, new_max_val) + recurse(node.right, new_max_val)
        
        return recurse(root, root.val)



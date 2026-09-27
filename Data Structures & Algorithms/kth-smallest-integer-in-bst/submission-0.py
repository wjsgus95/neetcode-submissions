# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num_visited = 0

        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal num_visited

            if not node:
                return
        
            left = traverse(node.left)

            num_visited += 1
            if k == num_visited:
                return node.val
            
            right = traverse(node.right) 

            if left is not None:
                return left
            if right is not None:
                return right
            
        return traverse(root)
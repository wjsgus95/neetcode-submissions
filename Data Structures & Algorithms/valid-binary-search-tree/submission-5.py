# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        
        def recurse(node: Optional[TreeNode]) -> bool:
            nonlocal prev

            if not node:
                return True
            
            if not recurse(node.left):
                return False
            
            if prev is None:
                prev = node.val
            else:
                if node.val <= prev:
                    return False
                prev = node.val
            
            if not recurse(node.right):
                return False
            
            return True
        
        return recurse(root)
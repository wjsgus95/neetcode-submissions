# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(left: Optional[TreeNode], right: Optioonal[TreeNode]) -> bool:
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            return recurse(left.left, right.left) and recurse(left.right, right.right)
        
        return recurse(p, q)
        
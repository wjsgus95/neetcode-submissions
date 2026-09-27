# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            return compare(node1.left, node2.left) and compare(node1.right, node2.right)
        
        def traverse(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            if compare(node, subRoot):
                return True
            
            return traverse(node.left) or traverse(node.right)
        
        return traverse(root)
        
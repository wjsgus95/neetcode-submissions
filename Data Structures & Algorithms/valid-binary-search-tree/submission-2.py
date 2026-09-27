# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        seen = []
        def visit(node: TreeNode) -> bool:
            if not seen:
                seen.append(node.val)
                return True
            else:
                result = seen[0] < node.val
                seen[0] = node.val
                return result

        def recurse(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            result = True
            if node.left:
                result = recurse(node.left)
            
            result = result and visit(node)

            if node.right:
                result = result and recurse(node.right)
            
            return result
        
        return recurse(root)
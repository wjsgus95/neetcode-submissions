# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightmost = dict()

        def get_level(index: int) -> int:
            level = 0
            while index > 1:
                index //= 2
                level += 1
            return level

        def recurse(index: int, node: Optional[TreeNode]): 
            if not node:
                return
            
            level = get_level(index)
            if not level in rightmost:
                rightmost[level] = node.val

            recurse(index * 2 + 1, node.right)
            recurse(index * 2, node.left)
        
        recurse(1, root)

        ans = []
        level = 0
        while level in rightmost:
            ans.append(rightmost[level])
            level += 1
        return ans
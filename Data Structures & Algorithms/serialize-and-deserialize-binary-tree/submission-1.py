# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []

        def recurse(node, index):
            while len(nodes) <= index:
                nodes.append(None)

            if not node:
                nodes[index] = None
                return
            else:
                nodes[index] = node.val

            recurse(node.left, index * 2)
            recurse(node.right, index * 2 + 1)

        recurse(root, 1)
        nodes = [str(v) if type(v) is int else '' for v in nodes]
        return "_".join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = [int(v) if v != '' else None for v in data.split('_')]

        def recurse(index: int) -> Optional[TreeNode]:
            if index >= len(nodes):
                return

            value = nodes[index] 
            if value is not None:
                node = TreeNode(value)
            else:
                return
            
            node.left = recurse(index * 2)
            node.right = recurse(index * 2 + 1)

            return node
        
        return recurse(1)

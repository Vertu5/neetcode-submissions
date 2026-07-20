# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    PREFIX = "#"
    NULL_NODE = ""

    def _serialize(self, node: Optional[TreeNode]) -> str:
        if not node:
            return self.NULL_NODE
            
        return f"{self.PREFIX}{node.val} {self._serialize(node.left)} {self._serialize(node.right)}"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_str = self._serialize(root)
        subRoot_str = self._serialize(subRoot)
        
        return subRoot_str in root_str
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # Dans la pile, on stocke : (le_noeud, sa_profondeur_actuelle)
        stack = [(root, 1)]
        profondeur_max = 0
        
        while stack:
            # On sort le nœud et la profondeur à laquelle il se trouve
            node, profondeur = stack.pop()
            
            # On met à jour notre record absolu
            profondeur_max = max(profondeur_max, profondeur)
            
            # On ajoute les enfants à la pile en leur donnant (profondeur du parent + 1)
            if node.left:
                stack.append((node.left, profondeur + 1))
            if node.right:
                stack.append((node.right, profondeur + 1))
                
        return profondeur_max
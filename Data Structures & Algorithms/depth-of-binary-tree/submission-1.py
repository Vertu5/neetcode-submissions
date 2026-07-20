# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = deque([root])
        compteur_profondeur = 0  # Votre compteur !
        
        while queue:
            # On regarde combien de nœuds il y a sur ce niveau précis
            taille_niveau = len(queue)
            
            # On vide tous les nœuds de ce niveau, et on ajoute leurs enfants
            for _ in range(taille_niveau):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # On a fini un étage complet, on incrémente le compteur
            compteur_profondeur += 1
            
        return compteur_profondeur
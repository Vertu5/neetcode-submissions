# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        # Le dictionnaire qui stocke nos signatures uniques
        self.hash_map = {}
        # L'ID (hash) de l'arbre que l'on recherche
        self.target_hash = None
        # Drapeau (flag) pour savoir si on l'a trouvé
        self.found = False

    def _compute_hash(self, node: Optional[TreeNode], is_target: bool) -> int:
        """
        Calcule et attribue un ID unique à chaque structure de sous-arbre.
        """
        # Cas de base : un nœud vide a toujours l'ID 0
        if not node:
            return 0

        # 1. On calcule l'ID de l'enfant gauche et droit (parcours Suffixe / Post-order)
        left_hash = self._compute_hash(node.left, is_target)
        right_hash = self._compute_hash(node.right, is_target)

        # 2. On crée la signature unique de ce nœud
        signature = (node.val, left_hash, right_hash)

        # 3. Si cette signature est nouvelle, on lui donne un nouvel ID
        if signature not in self.hash_map:
            self.hash_map[signature] = len(self.hash_map) + 1

        current_hash = self.hash_map[signature]

        # 4. Si on parcourt le grand arbre et que l'ID correspond, c'est gagné !
        if not is_target and current_hash == self.target_hash:
            self.found = True

        return current_hash

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Réinitialisation de l'état (très important sur LeetCode pour les tests successifs)
        self.hash_map = {}
        self.found = False
        self.target_hash = None
        
        # Étape 1 : Hacher l'arbre cible (subRoot) pour obtenir son ID
        self.target_hash = self._compute_hash(subRoot, is_target=True)
        
        # Étape 2 : Hacher le grand arbre (root) et chercher la correspondance
        self._compute_hash(root, is_target=False)
        
        return self.found
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Avantage : Totalement immunisé contre le Stack Overflow. Compare niveau par niveau.
    Inconvénient : Utilise plus de mémoire si l'arbre est très large.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # On place les deux racines ensemble dans la file
        queue = deque([(p, q)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            # Si les deux sont vides, on passe simplement aux suivants
            if not node1 and not node2:
                continue
            
            # Si un seul est vide ou valeurs différentes -> Faux
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # On ajoute les enfants par paires pour les comparer au prochain tour
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
            
        return True
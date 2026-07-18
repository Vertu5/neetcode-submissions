# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], retenue: int = 0) -> Optional[ListNode]:
        # Condition d'arrêt : on a fini de parcourir l1, l2 ET il n'y a plus de retenue
        if not l1 and not l2 and retenue == 0:
            return None
            
        # On récupère les valeurs de manière sécurisée (0 si la liste est vide)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # On calcule la somme pour ce niveau
        total = val1 + val2 + retenue
        
        # On crée le nœud actuel
        nouveau_noeud = ListNode(total % 10)
        
        # On calcule les prochains nœuds à envoyer à l'appel suivant
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        nouvelle_retenue = total // 10
        
        # LA MAGIE RÉCURSIVE : on attache le nœud actuel au résultat du reste de l'addition
        nouveau_noeud.next = self.addTwoNumbers(next1, next2, nouvelle_retenue)
        
        return nouveau_noeud
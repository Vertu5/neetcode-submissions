# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Le nœud factice nous sauve la vie si on doit supprimer le premier élément (head)
        dummy = ListNode(0, head)
        
        gauche = dummy
        droite = head
        
        # 1. On avance 'droite' de n positions pour créer l'écart
        for _ in range(n):
            droite = droite.next
            
        # 2. On avance les deux à la même vitesse jusqu'à la fin
        while droite:
            gauche = gauche.next
            droite = droite.next
            
        # 3. À ce stade, 'gauche' est juste AVANT le nœud à supprimer.
        # On applique votre logique : on saute le nœud !
        gauche.next = gauche.next.next
        
        # On renvoie la nouvelle liste (qui commence après notre dummy)
        return dummy.next
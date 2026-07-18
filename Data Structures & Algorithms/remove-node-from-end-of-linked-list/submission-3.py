class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # Fonction récursive interne
        def plonge_et_compte(noeud):
            # Condition d'arrêt : on a atteint la fin (None)
            if not noeud:
                return 0
            
            # On plonge jusqu'à la fin AVANT de compter
            compteur = plonge_et_compte(noeud.next) + 1
            
            # Si le compteur en remontant atteint (n + 1),
            # cela signifie qu'on est JUSTE AVANT le nœud à supprimer
            if compteur == n + 1:
                noeud.next = noeud.next.next
                
            return compteur
            
        plonge_et_compte(dummy)
        return dummy.next
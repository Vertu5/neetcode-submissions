class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # 1. On stocke tous les nœuds dans un tableau classique
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        # 2. On utilise deux pointeurs (début et fin du tableau)
        left = 0
        right = len(nodes) - 1
        
        # 3. On relie les nœuds en alternant
        while left < right:
            # Le nœud de gauche pointe vers le nœud de droite
            nodes[left].next = nodes[right]
            left += 1
            
            # Pour éviter de créer un cycle à la toute fin (si left == right)
            if left == right:
                break
                
            # Le nœud de droite pointe vers le NOUVEAU nœud de gauche
            nodes[right].next = nodes[left]
            right -= 1
            
        # TRÈS IMPORTANT : Le dernier nœud de notre nouvelle liste 
        # doit pointer vers None, sinon on crée un cycle infini !
        nodes[left].next = None
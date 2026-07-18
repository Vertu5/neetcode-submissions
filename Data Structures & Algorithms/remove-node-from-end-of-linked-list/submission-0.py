# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Notre fonction utilitaire (que vous connaissez bien maintenant !)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Étape 1 : On inverse toute la liste
        reversed_head = self.reverseList(head)
        
        # Étape 2 : On supprime le n-ième nœud en partant du NOUVEAU début
        dummy = ListNode(0, reversed_head)
        curr = dummy
        
        # On avance de (n - 1) pas pour se placer JUSTE AVANT le nœud à supprimer
        for _ in range(n - 1):
            curr = curr.next
            
        # On saute le n-ième nœud
        if curr.next:
            curr.next = curr.next.next
            
        # Étape 3 : On ré-inverse la liste pour la remettre dans l'ordre
        # (Attention : le nouveau point de départ est dummy.next)
        final_head = self.reverseList(dummy.next)
        
        return final_head
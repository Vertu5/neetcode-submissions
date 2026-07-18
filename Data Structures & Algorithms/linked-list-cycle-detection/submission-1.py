# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Notre "carnet de route" pour mémoriser les nœuds visités
        visited_nodes = set()
        
        curr = head
        while curr:
            # Si on a déjà vu ce nœud, c'est qu'il y a une boucle
            if curr in visited_nodes:
                return True
                
            # Sinon, on l'ajoute à l'ensemble et on avance
            visited_nodes.add(curr)
            curr = curr.next
            
        # On a atteint la fin de la liste
        return False
        
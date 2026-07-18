# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Les deux pointeurs partent de la ligne de départ
        slow = head
        fast = head
        
        # On doit vérifier fast et fast.next car le lièvre saute de 2 en 2
        while fast and fast.next:
            slow = slow.next          # La tortue avance de 1
            fast = fast.next.next     # Le lièvre avance de 2
            
            # Si les deux pointeurs pointent sur le même nœud, il y a un cycle
            if slow == fast:
                return True
                
        # Si la boucle while se termine, le lièvre a atteint la fin de la liste
        return False
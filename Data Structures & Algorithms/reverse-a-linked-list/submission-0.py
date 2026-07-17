# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # 1. Sauvegarder le reste de la liste
            next_node = curr.next
            
            # 2. Inverser le pointeur actuel
            curr.next = prev
            
            # 3. Avancer nos deux curseurs pour la prochaine itération
            prev = curr
            curr = next_node
            
        # À la fin, 'curr' est None et 'prev' pointe sur le nouveau début de la liste
        return prev
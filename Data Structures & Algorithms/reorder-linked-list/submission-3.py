from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        queue = deque()
        curr = head.next # On met tout sauf la tête dans la file
        
        while curr:
            queue.append(curr)
            curr = curr.next
            
        curr = head
        while queue:
            # On accroche le dernier élément (à droite)
            curr.next = queue.pop()
            curr = curr.next
            
            # S'il reste des éléments, on accroche le premier (à gauche)
            if queue:
                curr.next = queue.popleft()
                curr = curr.next
                
        # On ferme la liste pour éviter un cycle infini
        curr.next = None
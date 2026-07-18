from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        queue = deque()
        curr = head.next # On met tout sauf la tête
        while curr:
            queue.append(curr)
            curr = curr.next
            
        curr = head
        while queue:
            # On accroche le dernier élément
            curr.next = queue.poppop()
            curr = curr.next
            
            # S'il reste des éléments, on accroche le premier
            if queue:
                curr.next = queue.popleft()
                curr = curr.next
                
        curr.next = None # On ferme la liste
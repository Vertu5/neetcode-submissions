# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # On va modifier l1 sur place pour stocker le résultat
        curr1 = l1
        curr2 = l2
        prev = None
        retenue = 0
        
        # 1. On traverse les deux listes tant qu'elles ont toutes les deux des nœuds
        while curr1 and curr2:
            total = curr1.val + curr2.val + retenue
            curr1.val = total % 10
            retenue = total // 10
            
            prev = curr1
            curr1 = curr1.next
            curr2 = curr2.next
            
        # 2. Si l2 est plus longue que l1, on accroche le reste de l2 à la suite de l1
        if curr2:
            prev.next = curr2
            curr1 = curr2  # On bascule notre curseur principal sur la suite de l2
            
        # 3. On propage la retenue restante dans les nœuds restants (que ce soit l1 ou l2)
        while curr1:
            total = curr1.val + retenue
            curr1.val = total % 10
            retenue = total // 10
            
            prev = curr1
            curr1 = curr1.next
            
        # 4. S'il reste une retenue à la toute fin, on crée un unique dernier nœud
        if retenue > 0:
            prev.next = ListNode(retenue)
            
        return l1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        retenue = 0
        
        # On continue tant qu'il y a des nœuds dans l1 OU l2 OU qu'il reste une retenue
        while l1 or l2 or retenue:
            # Si une liste est plus courte que l'autre, on remplace le vide par 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calcul de la somme pour cette colonne
            total = val1 + val2 + retenue
            
            # La nouvelle retenue (ex: 15 // 10 = 1)
            retenue = total // 10
            
            # Le chiffre à écrire (ex: 15 % 10 = 5)
            curr.next = ListNode(total % 10)
            
            # On avance nos pointeurs
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
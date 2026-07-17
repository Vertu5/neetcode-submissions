# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Création du nœud factice pour simplifier la construction
        dummy = ListNode()
        tail = dummy
        
        # Tant qu'il reste des éléments dans les DEUX listes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # On avance le curseur de notre nouvelle liste
            tail = tail.next
            
        # Si une liste est vide, on accroche directement le reste de l'autre liste
        # En Python, 'list1 or list2' renvoie list1 si elle n'est pas vide, sinon list2
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # Le vrai début de la liste fusionnée est le suivant du nœud factice
        return dummy.next
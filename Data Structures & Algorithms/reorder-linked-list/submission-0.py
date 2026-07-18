# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        ## ÉTAPE 1 : Trouver le milieu de la liste (Lièvre et Tortue)
        # On décale un peu le lièvre au départ pour que la tortue 
        # s'arrête exactement à la fin de la première moitié
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # On coupe la liste en deux : 'second' est le début de la 2ème moitié
        second = slow.next
        slow.next = None  # On casse le lien pour séparer les deux listes
        
        ## ÉTAPE 2 : Inverser la deuxième moitié
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 'prev' pointe maintenant sur le nouveau début de notre 2ème moitié inversée
        
        ## ÉTAPE 3 : Fusionner les deux listes en alternant
        first = head
        second = prev # prev est la tête de notre liste inversée
        
        while second:
            # 1. On sauvegarde les "suivants" pour ne pas casser la chaîne
            tmp1 = first.next
            tmp2 = second.next
            
            # 2. On change les liens : 1er -> 2ème -> suite du 1er
            first.next = second
            second.next = tmp1
            
            # 3. On avance nos deux pointeurs pour le tour de boucle suivant
            first = tmp1
            second = tmp2
from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        COMPLEXITÉS :
        
        - Temps : O(N log k)
          La boucle 'for' parcourt les N éléments du tableau. Pour chaque élément, 
          les opérations d'insertion (heappush) et de suppression (heappop) dans 
          un tas de taille maximale k coûtent O(log k). 
          (Note: le tri final ajoute un coût de O(k log k) mais reste négligeable 
          face au parcours principal).
          
        - Espace : O(k)
          Le tas (max_heap) stocke simultanément un maximum de k + 1 éléments.
          L'utilisation de la mémoire grandit avec la valeur de k, et non avec 
          la taille totale du tableau N.
        """
        max_heap = []
        
        for num in arr:
            distance = abs(num - x)
            
            # On stocke (-distance, -valeur) pour inverser le comportement du tas
            heapq.heappush(max_heap, (-distance, -num))
            
            # On expulse l'élément le plus éloigné dès qu'on dépasse k
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        result = [-num for dist, num in max_heap]
        return sorted(result)
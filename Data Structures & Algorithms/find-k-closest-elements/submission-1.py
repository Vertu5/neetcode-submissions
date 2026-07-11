from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        COMPLEXITÉS :
        
        - Temps : O(log(N - k) + k)
          1. O(log(N - k)) : La boucle de recherche binaire ne parcourt pas le tableau, 
             elle divise l'espace de recherche par deux à chaque étape pour trouver le 
             point de départ de la fenêtre.
          2. O(k) : Une fois l'index 'left' trouvé, l'opération de "slicing" 
             arr[left:left + k] prend un temps proportionnel à la taille k pour 
             copier les éléments dans la liste de retour.
             
        - Espace : O(1)
          Seules des variables de position (left, right, mid) sont utilisées. Aucune 
          structure de données annexe n'est créée pendant la recherche.
        """
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left:left + k]
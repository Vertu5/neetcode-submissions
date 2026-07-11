from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        COMPLEXITÉS :
        
        - Temps : O(N - k)
          On commence avec une fenêtre de taille N (tout le tableau). À chaque itération, 
          on élimine 1 élément jusqu'à ce qu'il n'en reste que k. Cela fait exactement 
          N - k itérations, avec une comparaison en temps constant O(1) à l'intérieur.
          
        - Espace : O(1)
          L'algorithme n'utilise que deux variables entières (left et right) en mémoire, 
          quelle que soit la taille du tableau en entrée.
        """
        left = 0
        right = len(arr) - 1
        
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
                
        return arr[left:right + 1]
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n  # Initialise tout à 0 (gère automatiquement les jours sans réponse)
        stack = []     # Stocke les index des jours
        
        # On parcourt à l'envers : de la fin jusqu'à 0
        for i in range(n - 1, -1, -1):
            
            # Tant qu'il y a des éléments et que la temp. actuelle est >= à celle de la pile
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop() # Ces jours ne seront plus jamais la réponse pour les jours précédents
                
            # Si la pile n'est pas vide, le sommet est notre prochain jour plus chaud
            if stack:
                res[i] = stack[-1] - i
                
            # On ajoute le jour actuel à la pile pour les jours précédents
            stack.append(i)
            
        return res
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Approche avec File à double extrémité (Monotonic Deque).
        Complexité en temps : O(N) strict (coût amorti de O(1) par élément).
        Complexité en espace : O(k) car la file ne dépasse pas la taille k.
        """
        if not nums or k == 0:
            return []
            
        q = deque() # Ne stockera que les index des éléments utiles
        res = []
        
        for i in range(len(nums)):
            # 1. Péremption : on retire l'élément à gauche s'il sort de la fenêtre
            if q and q[0] == i - k:
                q.popleft()
            
            # 2. Compétition : on retire par la droite tous les éléments plus petits
            # que le nouvel arrivant (ils n'ont plus aucune chance d'être le max)
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            # 3. Ajout du nouvel index
            q.append(i)
            
            # 4. Enregistrement : le max est toujours à l'avant de la file
            # On enregistre seulement une fois que la première fenêtre de taille k est parcourue
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
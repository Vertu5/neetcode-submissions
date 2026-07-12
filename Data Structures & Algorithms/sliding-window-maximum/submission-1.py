from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Approche avec Max-Heap (File de priorité avec suppression paresseuse).
        Complexité en temps : O(N log N) dans le pire des cas.
        Complexité en espace : O(N) dans le pire des cas.
        """
        if not nums or k == 0:
            return []
            
        heap = [] 
        res = []
        
        # Initialisation de la première fenêtre
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        res.append(-heap[0][0])
        
        # Parcours du reste du tableau
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            
            # Nettoyage paresseux : suppression des éléments périmés au sommet
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
            
        return res
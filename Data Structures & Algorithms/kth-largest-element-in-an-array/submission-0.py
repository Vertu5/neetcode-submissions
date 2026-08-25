import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            
            # Dès qu'on dépasse k éléments, on éjecte le plus petit
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # Le sommet du Min-Heap contient le k-ième plus grand
        return min_heap[0]
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        O(N) - Sliding Window Approach (Optimal)
        """
        min_len = float('inf')
        current_sum = 0
        left = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window while the sum is valid
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_len if min_len != float('inf') else 0
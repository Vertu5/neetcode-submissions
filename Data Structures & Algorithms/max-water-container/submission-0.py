class Solution:
    def _calculate_area(self, height: list[int], left: int, right: int) -> int:
        """
        Private helper method to calculate the current water area.
        """
        width = right - left
        min_height = min(height[left], height[right])
        return width * min_height

    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 1. Calculate the area using our helper method
            current_area = self._calculate_area(height, left, right)
            
            # 2. Update the global maximum area
            max_area = max(max_area, current_area)
            
            # 3. The Greedy choice: move the pointer of the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
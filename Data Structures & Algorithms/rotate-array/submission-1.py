class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0: 
            return
        
        # Counter to track when we've successfully moved all N elements
        elements_moved = 0 
        start = 0
        
        while elements_moved < n:
            current_idx = start
            value_to_place = nums[start]
            
            while True:
                # Calculate the destination using modulo
                next_idx = (current_idx + k) % n
                
                # The Switch! Save the victim, place our current value
                temp = nums[next_idx]
                nums[next_idx] = value_to_place
                
                # The victim becomes the next value we need to place
                value_to_place = temp
                current_idx = next_idx
                elements_moved += 1
                
                # If we loop back to where this specific cycle started, break out
                if current_idx == start:
                    break
            
            # Move to the next index to start the next cycle (if elements remain)
            start += 1
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        n = len(nums)
        
        # ==========================================
        # PHASE 1: THE SETUP (Scouting the players)
        # ==========================================
        # We take the very first number and put it in Chair 1.
        candidate1 = nums[0]
        count1 = 1
        
        # Chair 2 is empty for now.
        candidate2 = None
        count2 = 0
        
        i = 1
        
        # We scan forward just enough to find a different number for Chair 2.
        while i < n:
            if nums[i] == candidate1:
                # Still the same number, just increase its count.
                count1 += 1
            else:
                # We found a completely different number! Put it in Chair 2.
                candidate2 = nums[i]
                count2 = 1
                i += 1 # Move to the next number before starting the main loop
                break  # Setup is done, exit this scouting loop
            i += 1
            
        # Edge Case Check: What if the whole array was just clones? (e.g., [2, 2, 2])
        if candidate2 is None:
            return [candidate1]
            
        # ==========================================
        # PHASE 2: THE BATTLE (Cancellation process)
        # ==========================================
        # We resume exactly at index 'i' where the setup loop left off.
        while i < n:
            num = nums[i]
            
            # Rule 1: Always check identity first
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
                
            # Rule 2: If a chair is empty, claim it
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
                
            # Rule 3: The number is different AND both chairs are taken.
            # We have 3 distinct elements. They cancel each other out!
            else:
                count1 -= 1
                count2 -= 1
                
            i += 1
            
        # ==========================================
        # PHASE 3: THE VERIFICATION (Counting survivors)
        # ==========================================
        # The candidates in the chairs are just "suspects". 
        # We must count their actual occurrences in the original array.
        verify_count1 = 0
        verify_count2 = 0
        
        for num in nums:
            if num == candidate1:
                verify_count1 += 1
            elif num == candidate2:
                verify_count2 += 1
                
        # ==========================================
        # PHASE 4: THE VERDICT
        # ==========================================
        result = []
        if verify_count1 > n // 3:
            result.append(candidate1)
        if verify_count2 > n // 3:
            result.append(candidate2)
            
        return result
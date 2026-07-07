from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # --- 1. Fast path for arrays with zeroes ---
        if 0 in nums:
            zero_count = 0
            zero_index = -1 
            non_zero_product = 1
            
            for i in range(len(nums)): 
                if nums[i] == 0:
                    zero_count += 1 
                    zero_index = i
                    # If there are two or more zeroes, every product will be 0
                    if zero_count == 2: 
                        return [0] * len(nums)
                else: 
                    non_zero_product *= nums[i]
            
            # If exactly one zero exists, everything is 0 except at that index
            result = [0] * len(nums)
            result[zero_index] = non_zero_product
            return result

        # --- 2. Prefix and Suffix approach for arrays without zeroes ---
        result = [1] * len(nums)

        # Calculate Prefix (product of all elements to the left)
        for i in range(1, len(nums)): 
            result[i] = result[i - 1] * nums[i - 1]

        # Calculate Suffix (product of all elements to the right)
        right_product = 1
        for i in range(len(nums) - 1, -1, -1): 
            result[i] = result[i] * right_product
            right_product *= nums[i] 

        return result
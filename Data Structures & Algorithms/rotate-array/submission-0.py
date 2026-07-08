class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 1. Modulo to avoid redundant full rotations
        k = k % n 
        
        # If there's nothing to rotate, stop early
        if k == 0:
            return

        # Helper function using your "two pointers" logic
        def reverse(left: int, right: int) -> None:
            while left < right:
                # tuple swap!
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the whole array
        reverse(0, n - 1)
        
        # Step 2: Reverse the first part (size k)
        reverse(0, k - 1)
        
        # Step 3: Reverse the second part (the remaining elements)
        reverse(k, n - 1)
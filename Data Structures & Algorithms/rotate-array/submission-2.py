class Solution:
    def _reverse(self, nums: list[int], left: int, right: int) -> None:
        """
        Helper method to reverse a portion of the array in-place.
        The '_' prefix indicates this is intended as a private method.
        """
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 
        
        if k == 0:
            return

        # Step 1: Reverse the whole array
        self._reverse(nums, 0, n - 1)
        
        # Step 2: Reverse the first part (size k)
        self._reverse(nums, 0, k - 1)
        
        # Step 3: Reverse the second part (the remaining elements)
        self._reverse(nums, k, n - 1)
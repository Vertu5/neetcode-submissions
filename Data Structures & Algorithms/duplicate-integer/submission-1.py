class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashnumber = set(nums)
        
        return len(hashnumber) != len(nums)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        hashnums = set()

        for num in nums:
            if num in hashnums:
                return True 
            
            hashnums.add(num)
        
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashnumber = set()
        for i in nums: 
            if i in hashnumber:
                return True 
            
            hashnumber.add(i)

        return False
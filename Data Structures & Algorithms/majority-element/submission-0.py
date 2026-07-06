#compte hashmap solution O(n) time and space O(n) globalement


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashcompt = {}

        for num in nums:
            hashcompt[num] =  hashcompt.get(num, 0) + 1
            if hashcompt[num] > len(nums)//2:
                return num
#compte hashmap solution O(n) time and space O(n) globalement


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidat, compteur = 0,0

        for num in nums:
            if compteur == 0: 
                candidat = num
            if candidat == num: 
                compteur += 1
            else : compteur -= 1
             
            #pas obligatoire mais j aime bien
            if compteur > len(nums) // 2: 
                return candidat

        return candidat    

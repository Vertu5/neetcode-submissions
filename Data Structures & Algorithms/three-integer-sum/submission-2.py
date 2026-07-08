# spatial complexity O(n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        resultats = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            deja_vus = set()
            j = i + 1
            while j < len(nums):
                # Le complément qu'on cherche pour arriver à 0
                complement = -(nums[i] + nums[j])
                
                if complement in deja_vus:
                    resultats.append([nums[i], nums[j], complement])
                    # Ignorer les doublons pour le 2ème nombre
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                        
                deja_vus.add(nums[j])
                j += 1
                
        return resultats
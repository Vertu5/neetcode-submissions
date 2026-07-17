class Solution:
    def search(self, nums: list[int], target: int) -> int:
        gauche = 0
        droite = len(nums) - 1
        
        while gauche <= droite:
            mid = (gauche + droite) // 2
            
            # 1. On a trouvé la cible
            if nums[mid] == target:
                return mid
                
            # 2. La moitié gauche est triée
            if nums[gauche] <= nums[mid]:
                # Le target est-il dans cette plage triée ?
                if nums[gauche] <= target < nums[mid]:
                    droite = mid - 1  # On cherche à gauche
                else:
                    gauche = mid + 1  # On cherche à droite
                    
            # 3. La moitié droite est triée
            else:
                # Le target est-il dans cette plage triée ?
                if nums[mid] < target <= nums[droite]:
                    gauche = mid + 1  # On cherche à droite
                else:
                    droite = mid - 1  # On cherche à gauche
                    
        # On a épuisé le tableau sans trouver la cible
        return -1
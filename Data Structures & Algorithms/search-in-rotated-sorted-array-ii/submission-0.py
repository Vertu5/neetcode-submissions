class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        gauche = 0
        droite = len(nums) - 1
        
        while gauche <= droite:
            mid = (gauche + droite) // 2
            
            # 1. On a trouvé la cible
            if nums[mid] == target:
                return True
                
            # 2. Le cas ambigu causé par les doublons
            if nums[gauche] == nums[mid] and nums[mid] == nums[droite]:
                gauche += 1
                droite -= 1
                continue  # On passe directement à l'itération suivante
                
            # 3. La moitié gauche est triée
            if nums[gauche] <= nums[mid]:
                if nums[gauche] <= target < nums[mid]:
                    droite = mid - 1
                else:
                    gauche = mid + 1
                    
            # 4. La moitié droite est triée
            else:
                if nums[mid] < target <= nums[droite]:
                    gauche = mid + 1
                else:
                    droite = mid - 1
                    
        return False
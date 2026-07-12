from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            # Si on trouve le nombre exact
            if target == nums[middle]:
                return middle
                
            # Si la cible est plus GRANDE que le milieu
            elif target > nums[middle]:
                
                # OU si la cible est plus petite que l'élément juste après
                if middle == len(nums) - 1 or target < nums[middle + 1]:
                    return middle + 1
                
                # Sinon, on continue à chercher dans la partie droite
                left = middle + 1
                
            # Si la cible est plus PETITE que le milieu
            else:

                # OU si la cible est plus grande que l'élément juste avant
                if middle == 0 or target > nums[middle - 1]:
                    return middle
                
                # Sinon, on continue à chercher dans la partie gauche
                right = middle - 1

        return 0
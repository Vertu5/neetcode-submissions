from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            if target == nums[middle]:
                return middle  # La cible est dans le tableau, on renvoie son index
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
                
        # Si on sort de la boucle, c'est qu'on n'a rien trouvé.
        # 'left' pointe naturellement sur le futur index d'insertion !
        return left
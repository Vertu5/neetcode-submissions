from typing import List
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        try:
            # 1. On cherche le premier zéro. 
            # Python s'arrête dès qu'il le trouve et nous donne sa position exacte.
            zero_index = nums.index(0)
            
        except ValueError:
            # 2. S'il n'y a aucun zéro, on fait notre méthode One-Pass (préfixe/suffixe)
            n = len(nums)
            result = [1] * n
            left_product = right_product = 1
            for i in range(n):
                result[i] *= left_product
                left_product *= nums[i]
                
                right_index = n - 1 - i
                result[right_index] *= right_product
                right_product *= nums[right_index]
            return result

        # --- Si on arrive ici, c'est qu'il y a au moins UN zéro ---

        # 3. TA LOGIQUE : On cherche un 2ème zéro en commençant APRÈS le premier !
        # On ne reparcourt pas le début du tableau.
        if 0 in nums[zero_index + 1:]:
            return [0] * len(nums)

        # 4. S'il n'y a qu'un seul zéro : 
        # On doit quand même multiplier les nombres qui étaient AVANT le zéro, 
        # mais on peut utiliser math.prod() qui est codé en C et ultra rapide.
        non_zero_product = math.prod(nums[:zero_index]) * math.prod(nums[zero_index + 1:])
        
        result = [0] * len(nums)
        result[zero_index] = non_zero_product
        return result
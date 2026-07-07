from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        left_product = 1
        right_product = 1
        
        for i in range(n):
            # 1. Appliquer le produit de gauche, puis le mettre à jour
            result[i] *= left_product
            left_product *= nums[i]
            
            # 2. Appliquer le produit de droite, puis le mettre à jour
            # n - 1 - i permet de partir de la fin du tableau vers le début
            right_index = n - 1 - i
            result[right_index] *= right_product
            right_product *= nums[right_index]
            
        return result
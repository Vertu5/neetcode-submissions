#No recursion feel easier and better to me

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if not nums or len(nums) <= 1:
            return nums
            
        n = len(nums)
        taille_bloc = 1  # On commence en considérant des blocs de 1 seul élément
        
        # Tant que la taille de nos blocs est plus petite que le tableau entier
        while taille_bloc < n:
            
            # On parcourt le tableau de gauche à droite, en sautant de bloc en bloc
            for left in range(0, n, 2 * taille_bloc):
                
                # On calcule où se trouve le milieu et la fin de notre fusion actuelle.
                # (Le "min" sert à ne pas déborder si le tableau a une taille impaire)
                middle = min(left + taille_bloc - 1, n - 1)
                right = min(left + 2 * taille_bloc - 1, n - 1)
                
                # On ne lance la fusion que si on a vraiment un bloc de droite à fusionner
                if middle < right:
                    self.merge(nums, left, middle, right)
            
            # Une fois qu'on a balayé tout le tableau, on double la taille des blocs !
            # Les blocs de 1 deviennent des blocs de 2, puis 4, puis 8...
            taille_bloc *= 2
            
        return nums

    def merge(self, nums: list[int], left: int, middle: int, right: int):
        # --- C'est EXACTEMENT le même code qu'avant ! ---
        copie_gauche = nums[left : middle + 1]
        copie_droite = nums[middle + 1 : right + 1]
        
        i = 0
        j = 0
        k = left
        
        while i < len(copie_gauche) and j < len(copie_droite):
            if copie_gauche[i] <= copie_droite[j]:
                nums[k] = copie_gauche[i]
                i += 1
            else:
                nums[k] = copie_droite[j]
                j += 1
            k += 1
            
        while i < len(copie_gauche):
            nums[k] = copie_gauche[i]
            i += 1
            k += 1
            
        while j < len(copie_droite):
            nums[k] = copie_droite[j]
            j += 1
            k += 1
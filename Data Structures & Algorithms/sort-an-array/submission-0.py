#recursive sort merge 

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Cas de base de sécurité
        if not nums or len(nums) <= 1:
            return nums
            
        # Lancement de l'algorithme sur l'ensemble du tableau
        self.divide(nums, 0, len(nums) - 1)
        
        # Le tableau 'nums' a été modifié sur place
        return nums

    def divide(self, nums: list[int], left: int, right: int):
        # 1. Condition de survie (cas de base)
        if left >= right:
            return
            
        # 2. Calcul du milieu
        middle = (left + right) // 2
        
        # 3. Appels récursifs pour diviser jusqu'au fond
        self.divide(nums, left, middle)
        self.divide(nums, middle + 1, right)

        # 4. Le vrai travail : on fusionne en remontant
        self.merge(nums, left, middle, right)


    def merge(self, nums: list[int], left: int, middle: int, right: int):
        # --- ÉTAPE 1 : Sauvegarde ---
        # On copie les éléments pour ne pas les perdre quand on va écraser 'nums'
        copie_gauche = nums[left : middle + 1]
        copie_droite = nums[middle + 1 : right + 1]
        
        # --- ÉTAPE 2 : Les 3 pointeurs ---
        i = 0       # Pointeur pour copie_gauche
        j = 0       # Pointeur pour copie_droite
        k = left    # Pointeur pour le tableau final nums
        
        # --- ÉTAPE 3 : La Bataille ---
        # Tant qu'il reste des éléments dans les DEUX listes
        while i < len(copie_gauche) and j < len(copie_droite):
            if copie_gauche[i] <= copie_droite[j]:
                nums[k] = copie_gauche[i]
                i += 1
            else:
                nums[k] = copie_droite[j]
                j += 1
            
            # Dans tous les cas, on avance sur le tableau final
            k += 1
            
        # --- ÉTAPE 4 : Ramasser les restes ---
        # Si la liste de droite s'est vidée en premier, on vide la gauche
        while i < len(copie_gauche):
            nums[k] = copie_gauche[i]
            i += 1
            k += 1
            
        # Si la liste de gauche s'est vidée en premier, on vide la droite
        while j < len(copie_droite):
            nums[k] = copie_droite[j]
            j += 1
            k += 1
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. On trie le tableau (crucial pour les deux pointeurs et les doublons)
        nums.sort()
        resultats = []
        
        # 2. On boucle pour "fixer" le premier nombre
        for i in range(len(nums)):
            
            # Petite optimisation : si le plus petit nombre est > 0, 
            # impossible que la somme de 3 nombres soit 0. On peut arrêter.
            if nums[i] > 0:
                break
            
            # On ignore les doublons pour le 1er nombre
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. Technique des deux pointeurs (comme Two Sum II)
            gauche = i + 1
            droite = len(nums) - 1
            
            while gauche < droite:
                somme_actuelle = nums[i] + nums[gauche] + nums[droite]
                
                if somme_actuelle == 0:
                    # On a trouvé un triplet !
                    resultats.append([nums[i], nums[gauche], nums[droite]])
                    
                    # On avance le pointeur gauche et on recule le droit
                    gauche += 1
                    droite -= 1
                    
                    # On ignore les doublons pour le 2ème nombre (le pointeur gauche)
                    # (Pas besoin de le faire pour la droite, la somme s'ajustera d'elle-même)
                    while gauche < droite and nums[gauche] == nums[gauche - 1]:
                        gauche += 1
                        
                elif somme_actuelle < 0:
                    # La somme est trop petite, on augmente gauche
                    gauche += 1
                else:
                    # La somme est trop grande, on diminue droite
                    droite -= 1
                    
        return resultats
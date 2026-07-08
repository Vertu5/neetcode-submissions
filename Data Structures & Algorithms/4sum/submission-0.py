class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        resultats = []
        n = len(nums)
        
        # 1. On fixe le 1er nombre
        for i in range(n - 3):
            # Ignorer les doublons pour le 1er nombre
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # --- OPTIMISATIONS EXTRÊMES ---
            # Si les 4 plus petits nombres restants dépassent la cible, on arrête tout
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Si le nombre actuel + les 3 plus grands n'atteignent pas la cible, on passe au suivant
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
                
            # 2. On fixe le 2ème nombre
            for j in range(i + 1, n - 2):
                # Ignorer les doublons pour le 2ème nombre
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # --- OPTIMISATIONS EXTRÊMES (Niveau j) ---
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                    
                # 3. La technique des Deux Pointeurs
                gauche = j + 1
                droite = n - 1
                
                while gauche < droite:
                    somme = nums[i] + nums[j] + nums[gauche] + nums[droite]
                    
                    if somme == target:
                        resultats.append([nums[i], nums[j], nums[gauche], nums[droite]])
                        gauche += 1
                        droite -= 1
                        
                        # Ignorer les doublons pour le 3ème nombre (gauche)
                        while gauche < droite and nums[gauche] == nums[gauche - 1]:
                            gauche += 1
                        # Ignorer les doublons pour le 4ème nombre (droite)
                        while gauche < droite and nums[droite] == nums[droite + 1]:
                            droite -= 1
                            
                    elif somme < target:
                        gauche += 1
                    else:
                        droite -= 1
                        
        return resultats
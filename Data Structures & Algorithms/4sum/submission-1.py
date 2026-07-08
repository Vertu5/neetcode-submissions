class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        resultats = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Mêmes optimisations
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Mêmes optimisations
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                    
                # 3. Technique du HashSet pour les 2 derniers nombres
                cible_2sum = target - nums[i] - nums[j]
                deja_vus = set()
                k = j + 1
                
                while k < n:
                    complement = cible_2sum - nums[k]
                    
                    if complement in deja_vus:
                        resultats.append([nums[i], nums[j], complement, nums[k]])
                        
                        # Ignorer les doublons pour le 4ème nombre
                        while k + 1 < n and nums[k] == nums[k + 1]:
                            k += 1
                            
                    # On ajoute le nombre actuel au set (APRÈS avoir vérifié le complément)
                    deja_vus.add(nums[k])
                    k += 1
                    
        return resultats
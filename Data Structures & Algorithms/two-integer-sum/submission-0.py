class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. On initialise notre dictionnaire vide
        # Il stockera les données sous la forme {valeur_du_nombre: son_index}
        deja_vus = {} 
        
        # 2. On parcourt le tableau en récupérant à la fois l'index (i) et la valeur (num)
        for i in range(len(nums)):
            num = nums[i]
            
            # 3. On calcule le complément qu'on cherche
            difference = target - num
            
            # 4. On vérifie si ce complément est DÉJÀ dans notre dictionnaire
            if difference in deja_vus:
                # Si oui, on a trouvé notre paire ! 
                # On renvoie l'index du complément enregistré, et notre index actuel (i)
                return [deja_vus[difference], i]
            
            # 5. Si non, on ajoute le nombre actuel au dictionnaire pour la suite
            deja_vus[num] = i
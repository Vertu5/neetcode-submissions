class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # HashMap pour stocker les éléments sous la forme {valeur: dernier_index_vu}
        num_map = {} 

        for i, num in enumerate(nums):
            # Si le nombre existe déjà dans la map
            if num in num_map:
                # On récupère son ancien index et on vérifie la distance
                if i - num_map[num] <= k:
                    return True
            
            # On ajoute ou met à jour la valeur dans la map avec l'index actuel (i).
            # Il est crucial de mettre à jour avec l'index le plus récent pour 
            # minimiser la distance (i - j) pour les prochaines itérations.
            num_map[num] = i
            
        return False
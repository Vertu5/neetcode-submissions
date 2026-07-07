class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return count
        # On initialise notre "carnet de voyage" (le Hash Map).
        # Le {0: 1} est crucial : il signifie qu'avant même de commencer, 
        # on a virtuellement vu une somme de 0 exactement une fois.
        prefix_sums = {0: 1}
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            # 1. On avance d'un pas et on met à jour notre somme totale depuis le début
            current_sum += num
            
            # 2. On calcule notre "point de départ parfait" dans le passé
            target_in_past = current_sum - k
            
            # 3. Si on a déjà croisé ce point de départ, bingo ! 
            # On ajoute le nombre de fois qu'on l'a vu à notre compteur de victoires.
            if target_in_past in prefix_sums:
                total_subarrays += prefix_sums[target_in_past]
                
            # 4. Avant de passer au nombre suivant, on note notre somme actuelle 
            # dans le carnet de voyage pour que les prochains nombres puissent l'utiliser.
            # (La méthode .get() permet de rajouter 1 si la somme existe déjà, ou d'initialiser à 0 + 1 sinon)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
                
        return total_subarrays        

        

        
        
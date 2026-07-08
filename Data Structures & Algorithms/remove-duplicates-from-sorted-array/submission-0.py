class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Si le tableau est vide, il y a 0 élément unique
        if not nums:
            return 0
            
        # Le pointeur d'écriture commence à 1 (car nums[0] est forcément unique)
        write_index = 1
        
        # Le pointeur de lecture parcourt le tableau à partir de l'index 1
        for read_index in range(1, len(nums)):
            
            # Si le nombre actuel est DIFFÉRENT du nombre précédent, 
            # c'est qu'on a trouvé un nouveau nombre unique !
            if nums[read_index] != nums[read_index - 1]:
                
                # On l'écrit à l'emplacement prévu par le pointeur d'écriture
                nums[write_index] = nums[read_index]
                
                # On avance le pointeur d'écriture pour le prochain nombre unique
                write_index += 1
                
        # Le pointeur d'écriture représente exactement le nombre (k) d'éléments uniques trouvés
        return write_index
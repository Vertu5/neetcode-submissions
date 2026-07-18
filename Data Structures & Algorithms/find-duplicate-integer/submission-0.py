class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1 : Le lièvre et la tortue pour trouver l'intersection
        tortue = nums[0]
        lievre = nums[0]
        
        while True:
            tortue = nums[tortue]           # Avance de 1
            lievre = nums[nums[lievre]]     # Avance de 2
            
            if tortue == lievre:
                break
                
        # Phase 2 : Trouver le point d'entrée du cycle (le doublon)
        tortue = nums[0]  # On remet la tortue sur la ligne de départ
        
        # Le lièvre reste là où il est, mais on le ralentit à la vitesse de la tortue
        while tortue != lievre:
            tortue = nums[tortue]
            lievre = nums[lievre]
            
        # Quand ils se croisent, c'est sur le nombre dupliqué
        return tortue
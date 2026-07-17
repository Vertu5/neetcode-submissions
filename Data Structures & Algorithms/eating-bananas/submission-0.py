class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        gauche, droite = 1, max(piles)
        
        while gauche < droite:
            mid = (gauche + droite) // 2
            
            # Calcul du temps total avec l'astuce de division entière
            heures_totales = 0
            for pile in piles:
                heures_totales += (pile + mid - 1) // mid
                
            if heures_totales <= h:
                # Koko finit à temps : on essaie de trouver une vitesse plus lente
                droite = mid 
            else:
                # Koko est trop lente : il faut augmenter la vitesse minimum
                gauche = mid + 1
                
        return gauche
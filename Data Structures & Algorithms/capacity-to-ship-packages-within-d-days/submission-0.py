class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # Les bornes de notre recherche
        gauche = max(weights)
        droite = sum(weights)
        
        while gauche < droite:
            mid = (gauche + droite) // 2
            
            # Simulation : combien de jours faut-il avec un bateau de capacité 'mid' ?
            jours_necessaires = 1
            poids_actuel = 0
            
            for poids in weights:
                # Si ajouter ce colis dépasse la capacité, on passe au jour suivant
                if poids_actuel + poids > mid:
                    jours_necessaires += 1
                    poids_actuel = poids # Ce colis est le premier du nouveau jour
                else:
                    poids_actuel += poids
                    
            # Si on réussit dans les temps (ou plus vite), on tente de réduire le bateau
            if jours_necessaires <= days:
                droite = mid
            # Si on met trop de temps, le bateau est trop petit
            else:
                gauche = mid + 1
                
        return gauche
class Solution:
    def _calculate_water(self, current_height: int, current_max: int) -> tuple[int, int]:
        """
        Fonction d'assistance privée pour calculer l'eau piégée sur UNE SEULE colonne.
        Retourne un tuple : (nouveau_maximum_historique, eau_piegee_sur_cette_colonne)
        """
        # 1. On met à jour le mur le plus haut vu jusqu'à présent de ce côté.
        # Si la colonne actuelle est plus grande que notre max historique, elle devient le nouveau max.
        updated_max = max(current_max, current_height)
        
        # 2. L'eau piégée est simplement la différence entre le plus haut mur 
        # qui nous protège et la hauteur du sol (la colonne) là où l'on se trouve.
        water_trapped = updated_max - current_height
        
        return updated_max, water_trapped

    def trap(self, height: list[int]) -> int:
        # Sécurité : si le tableau est vide, il n'y a pas d'eau à piéger.
        if not height:
            return 0
            
        # Initialisation des deux pointeurs aux extrémités du tableau
        left = 0
        right = len(height) - 1
        
        # Ces variables mémorisent le plus grand mur rencontré depuis la gauche ET depuis la droite.
        # Au départ, ce sont simplement les murs sur lesquels se trouvent nos pointeurs.
        max_left = height[left]
        max_right = height[right]
        
        # Le compteur global que l'on va renvoyer à la fin
        total_water = 0
        
        # On resserre l'étau jusqu'à ce que les deux pointeurs se rejoignent
        while left < right:
            
            # C'EST LA LIGNE LA PLUS IMPORTANTE DE L'ALGORITHME :
            # L'eau est toujours bloquée par le mur le plus petit. 
            # Si le mur max à gauche est plus petit que le mur max à droite, 
            # alors on est CERTAIN que c'est le mur de gauche qui va limiter l'eau pour le pointeur 'left'.
            if max_left < max_right:
                # On avance le pointeur gauche vers l'intérieur
                left += 1
                
                # On calcule l'eau pour cette nouvelle position et on met à jour le max_left
                max_left, water = self._calculate_water(height[left], max_left)
                
                # On ajoute l'eau trouvée au grand total
                total_water += water
                
            # Si le mur max à droite est plus petit (ou égal) au mur max à gauche,
            # alors c'est le côté droit qui est le goulot d'étranglement. On traite donc la droite.
            else:
                # On recule le pointeur droit vers l'intérieur
                right -= 1
                
                # On fait exactement le même calcul, mais vu depuis la droite
                max_right, water = self._calculate_water(height[right], max_right)
                
                # On ajoute l'eau trouvée au grand total
                total_water += water
                
        # Une fois que les pointeurs se sont rejoints, on a parcouru toutes les colonnes.
        return total_water
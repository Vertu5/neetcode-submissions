class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Idée : Au lieu de ramper, on mémorise l'index de chaque "erreur". 
        Quand on dépasse 'k', on saute directement par-dessus les lettres identiques 
        pour atterrir juste après la plus ancienne erreur !
        Complexité : O(26 * N) mais beaucoup plus rapide en pratique que la solution 1.
        """
        max_longueur = 0
        lettres_uniques = set(s)
        
        for cible in lettres_uniques:
            left = 0
            remplacements_utilises = 0
            file_erreurs = deque() # File d'attente pour mémoriser l'index des erreurs
            
            for right in range(len(s)):
                if s[right] != cible:
                    remplacements_utilises += 1
                    file_erreurs.append(right) # On garde l'index de cette erreur
                
                if remplacements_utilises > k:
                    # SAUT MAGIQUE : On récupère la plus vieille erreur et on saute juste après
                    plus_vieille_erreur = file_erreurs.popleft()
                    left = plus_vieille_erreur + 1
                    remplacements_utilises -= 1
                
                max_longueur = max(max_longueur, right - left + 1)
                
        return max_longueur
        
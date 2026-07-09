class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Idée : On teste chaque lettre de l'alphabet présente dans la chaîne.
        Si on rencontre une autre lettre, on utilise un remplacement.
        Si on n'a plus de remplacements, on fait avancer le pointeur 'left' PAS à PAS.
        Complexité : O(26 * N)
        """
        max_longueur = 0
        lettres_uniques = set(s)
        
        for cible in lettres_uniques:
            left = 0
            remplacements_utilises = 0
            
            for right in range(len(s)):
                if s[right] != cible:
                    remplacements_utilises += 1
                
                # On rampe (pas à pas) pour récupérer des remplacements
                while remplacements_utilises > k:
                    if s[left] != cible:
                        remplacements_utilises -= 1
                    left += 1
                
                max_longueur = max(max_longueur, right - left + 1)
                
        return max_longueur
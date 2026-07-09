class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Idée : Au lieu de comparer les 26 cases du tableau à chaque mouvement (O(26)),
        on garde en mémoire le nombre de lettres qui ont la MÊME fréquence (les "matches").
        Si on a 26 matchs, on a une permutation exacte !
        Complexité : O(N) Temps pur (pas de * 26), O(1) Espace.
        """
        if len(s1) > len(s2):
            return False
            
        count1 = [0] * 26
        count2 = [0] * 26
        
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        # Compter les matchs initiaux
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
                
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # --- Ajout du nouveau caractère (RIGHT) ---
            index_right = ord(s2[right]) - ord('a')
            count2[index_right] += 1
            
            if count1[index_right] == count2[index_right]:
                matches += 1
            elif count1[index_right] + 1 == count2[index_right]:
                # On vient de casser un match
                matches -= 1
                
            # --- Retrait de l'ancien caractère (LEFT) ---
            index_left = ord(s2[left]) - ord('a')
            count2[index_left] -= 1
            
            if count1[index_left] == count2[index_left]:
                matches += 1
            elif count1[index_left] - 1 == count2[index_left]:
                # On vient de casser un match
                matches -= 1
                
            left += 1
            
        return matches == 26
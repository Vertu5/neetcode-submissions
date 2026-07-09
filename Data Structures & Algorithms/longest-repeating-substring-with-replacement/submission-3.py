class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Idée : Identique à la Solution 3, mais on remplace le dictionnaire par
        un tableau de 26 zéros. L'accès à un tableau par index est beaucoup
        plus rapide pour le processeur que le hachage d'un dictionnaire.
        C'est la solution la plus performante possible pour ce problème !
        Complexité : O(N) Temps ultra-rapide, O(1) Espace constant
        """
        # Tableau de 26 cases (pour A à Z)
        counts = [0] * 26 
        max_freq = 0
        left = 0
        max_longueur = 0
        
        for right in range(len(s)):
            # ord('A') donne 65. Si s[right] est 'C' (67), l'index sera 67 - 65 = 2.
            index_char = ord(s[right]) - ord('A')
            counts[index_char] += 1
            
            max_freq = max(max_freq, counts[index_char])
            
            if (right - left + 1) - max_freq > k:
                index_left = ord(s[left]) - ord('A')
                counts[index_left] -= 1
                left += 1
            
            max_longueur = max(max_longueur, right - left + 1)
            
        return max_longueur 
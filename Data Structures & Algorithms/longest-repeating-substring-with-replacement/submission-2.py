class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Idée : Un seul passage. On compte la fréquence de chaque lettre.
        Condition de validité : (Taille Fenêtre) - (Fréquence Max) <= k
        Complexité : O(N) Temps, O(26) Espace
        """
        frequences = {}
        max_freq = 0
        left = 0
        max_longueur = 0
        
        for right in range(len(s)):
            caractere = s[right]
            frequences[caractere] = frequences.get(caractere, 0) + 1
            max_freq = max(max_freq, frequences[caractere])
            
            # Si la fenêtre est invalide, on la décale vers la droite (sans la rétrécir)
            if (right - left + 1) - max_freq > k:
                frequences[s[left]] -= 1
                left += 1
            
            max_longueur = max(max_longueur, right - left + 1)
            
        return max_longueur

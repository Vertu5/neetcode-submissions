class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            # Avancer le pointeur gauche s'il n'est pas sur un caractère alphanumérique
            while l < r and not s[l].isalnum():
                l += 1
            
            # Reculer le pointeur droit s'il n'est pas sur un caractère alphanumérique
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Comparaison (en minuscules pour être case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            # Continuer à avancer vers le centre
            l += 1
            r -= 1
            
        return True
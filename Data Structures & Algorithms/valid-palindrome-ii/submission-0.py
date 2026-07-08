class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 1. Nettoyage : on garde uniquement l'alphanumérique en minuscules
        cleaned_chars = [c.lower() for c in s if c.isalnum()]
        
        # Initialisation propre avec le "tuple unpacking"
        l, r = 0, len(cleaned_chars) - 1
        
        while l < r:
            if cleaned_chars[l] != cleaned_chars[r]:
                # Check si on fait un decalage on aura toujours un palindrome 
                return (self._is_palindrome_range(cleaned_chars, l + 1, r) or 
                        self._is_palindrome_range(cleaned_chars, l, r - 1))
            
            l += 1
            r -= 1
            
        return True

    def _is_palindrome_range(self, chars: list[str], left: int, right: int) -> bool:
        """
        Méthode privée : Vérifie si une portion d'un tableau de caractères 
        est un palindrome parfait.
        """
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
            
        return True
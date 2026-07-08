import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Nettoyage rapide via Regex
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Vérification avec deux pointeurs
        l = 0
        r = len(cleaned) - 1
        
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
            
        return True
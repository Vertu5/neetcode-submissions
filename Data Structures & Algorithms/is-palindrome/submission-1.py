import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. On remplace tout ce qui n'est ni lettre ni chiffre par du vide
        # et on met tout en minuscules.
        cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # 2. On compare la chaîne nettoyée avec son inverse
        return cleaned_str == cleaned_str[::-1]
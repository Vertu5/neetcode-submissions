class Solution:
    def isPalindrome(self, s: str) -> bool:
        # On filtre la chaîne pour ne garder que l'alphanumérique en minuscules
        cleaned_str = [c.lower() for c in s if c.isalnum()]
        
        # On compare la liste avec sa version inversée
        return cleaned_str == cleaned_str[::-1]
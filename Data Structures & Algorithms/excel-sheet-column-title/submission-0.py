class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # 1. On applique ton idée du -1 pour ramener sur un index 0-25
            columnNumber -= 1
            
            # 2. On trouve le reste pour identifier la lettre
            remainder = columnNumber % 26
            
            # 3. On ajoute la lettre au résultat
            result.append(chr(ord('A') + remainder))
            
            # 4. On passe à l'unité supérieure avec la division entière
            columnNumber //= 26
            
        # 5. On inverse la liste et on la transforme en chaîne de caractères
        return "".join(result[::-1])
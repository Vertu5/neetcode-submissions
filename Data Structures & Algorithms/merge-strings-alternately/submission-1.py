class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = [] # On utilise une liste pour la performance
        
        while i < len(word1) or j < len(word2):
            # Prendre une lettre du mot 1 si possible
            if i < len(word1):
                res.append(word1[i])
                i += 1
                
            # Prendre une lettre du mot 2 si possible
            if j < len(word2):
                res.append(word2[j])
                j += 1

        # On assemble la liste en une seule chaîne à la fin
        return "".join(res)
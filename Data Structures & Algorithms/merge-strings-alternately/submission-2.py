class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        
        # On alterne tant que l'on a des lettres dans les DEUX mots
        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1
            
        # On ajoute le reste éventuel du mot 1 (si i dépasse, ça ajoute juste du vide)
        res.append(word1[i:])
        
        # On ajoute le reste éventuel du mot 2
        res.append(word2[i:])
        
        return "".join(res)
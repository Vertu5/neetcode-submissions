class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. On compte les fréquences à la main dans un dictionnaire
        compteur = {}
        for num in nums:
            # .get(num, 0) renvoie 0 si le nombre n'existe pas encore
            compteur[num] = compteur.get(num, 0) + 1
            
        # 2. On trie les clés du dictionnaire en se basant sur leurs valeurs (fréquences)
        # key=lambda x: compteur[x] dit au trieur : "Ne trie pas selon le chiffre, trie selon sa fréquence"
        cles_triees = sorted(compteur.keys(), key=lambda x: compteur[x], reverse=True)
        
        # 3. On retourne les k premiers
        return cles_triees[:k]
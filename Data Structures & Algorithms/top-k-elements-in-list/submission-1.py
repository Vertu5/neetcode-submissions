class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        
        # 1. Compter les fréquences manuellement (Hashmap)
        compteur = {}
        for num in nums:
            compteur[num] = compteur.get(num, 0) + 1
            
        # 2. Créer les seaux (Buckets)
        # On crée un tableau de (n + 1) sous-tableaux vides.
        # L'index du seau = la fréquence.
        seaux = [[] for _ in range(n + 1)]
        
        # Remplir les seaux
        for num, freq in compteur.items():
            seaux[freq].append(num)
            
        # 3. Récolter les éléments en partant de la fin (les plus fréquents)
        resultat = []
        # On parcourt le tableau des seaux à l'envers (de n jusqu'à 0)
        for i in range(n, 0, -1):
            if seaux[i]:  # Si le seau n'est pas vide
                # On ajoute tous les nombres de ce seau à notre résultat
                resultat.extend(seaux[i])
                
                # Dès qu'on a atteint la quantité k demandée, on s'arrête
                if len(resultat) == k:
                    return resultat
                    
        return resultat
class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Idée : On utilise deux tableaux de taille 26 (comme des HashMaps ultra-rapides) 
        pour compter les fréquences. On fait glisser une fenêtre de la taille exacte de s1.
        Complexité : O(26 * N) -> O(N) Temps, O(1) Espace.
        """
        if len(s1) > len(s2):
            return False
            
        count1 = [0] * 26
        count2 = [0] * 26
        
        # 1. Initialiser la première fenêtre (taille len(s1))
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        # Si la première fenêtre est déjà une permutation
        if count1 == count2:
            return True
            
        # 2. Faire glisser la fenêtre sur le reste de s2
        # On ajoute le nouveau caractère à droite, on retire l'ancien à gauche
        for i in range(len(s1), len(s2)):
            nouveau_char = ord(s2[i]) - ord('a')
            ancien_char = ord(s2[i - len(s1)]) - ord('a')
            
            count2[nouveau_char] += 1
            count2[ancien_char] -= 1
            
            # En Python, comparer deux tableaux de taille 26 est très rapide (O(26))
            if count1 == count2:
                return True
                
        return False
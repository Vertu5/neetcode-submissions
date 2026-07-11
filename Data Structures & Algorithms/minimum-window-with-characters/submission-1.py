class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        COMPLEXITÉS (Version Table de Hachage) :
        
        - Temps : O(|S| + |T|)
          Similaire à l'approche tableau. On parcourt 't' pour remplir le dictionnaire, 
          puis on utilise nos deux pointeurs (left, right) pour traverser 's'. 
          La vérification (char in char_count) prend O(1) en moyenne grâce à la 
          table de hachage.
          
        - Espace : O(U) où U est le nombre de caractères UNIQUES dans 't'.
          Théoriquement, c'est plus optimisé que le tableau fixe de 128 si 't' 
          ne contient que 3 lettres différentes (le dictionnaire n'aura que 3 clés).
          Dans le pire des cas (toutes les lettres de l'alphabet), l'espace reste O(1) 
          car la taille de l'alphabet est bornée.
        """
        if len(t) > len(s) or not t:
            return ""
            
        # On ne stocke QUE les caractères présents dans 't'
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1
            
        left = 0
        min_len = float('inf')
        min_start = 0
        required = len(t)
        
        for right in range(len(s)):
            char_r = s[right]
            
            # Si le caractère fait partie de notre cible 't'
            if char_r in char_count:
                # S'il nous en manquait encore, on décrémente notre besoin total
                if char_count[char_r] > 0:
                    required -= 1
                # On met à jour le dictionnaire (peut devenir négatif si on a un excès)
                char_count[char_r] -= 1
                
            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                char_l = s[left]
                
                # Quand on rétrécit, on ne s'occupe que des caractères qui sont dans 't'
                if char_l in char_count:
                    char_count[char_l] += 1
                    # Si on repasse en positif, ça veut dire qu'il nous manque 
                    # à nouveau ce caractère pour valider la fenêtre
                    if char_count[char_l] > 0:
                        required += 1
                        
                left += 1
                
        return s[min_start : min_start + min_len] if min_len != float('inf') else ""
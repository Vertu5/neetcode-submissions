from typing import List

class Solution:
    """
    COMPLEXITÉS :
    
    - Temps : O(|S| + |T|)
    1. O(|T|) pour construire le tableau initial des fréquences.
    2. O(|S|) pour parcourir la chaîne 's'. Le pointeur 'right' traverse 's' 
        exactement une fois. Le pointeur 'left', malgré la boucle while, 
        ne recule jamais et traversera 's' au maximum une seule fois. 
        Chaque caractère est donc traité au maximum deux fois (ajouté puis retiré), 
        ce qui garantit un temps d'exécution strictement linéaire.
        
    - Espace : O(1) (Espace auxiliaire)
    L'algorithme alloue un tableau statique 'char_count' de 128 cases, qui 
    représente la table ASCII. Cette taille reste fixe (128 entiers) que 's' 
    fasse 10 caractères ou 10 millions. Les autres variables sont de simples 
    pointeurs (entiers). L'empreinte mémoire auxiliaire est donc constante.
    """
    def minWindow(self, s: str, t: str) -> str:
        # Si la cible est plus longue que la chaîne, c'est impossible
        if len(t) > len(s) or not t:
            return ""
            
        # Tableau ASCII de 128 cases initialisé à 0
        char_count = [0] * 128
        
        # On enregistre les lettres requises par t
        for char in t:
            char_count[ord(char)] += 1
            
        # Variables pour la fenêtre glissante
        left = 0
        min_len = float('inf')
        min_start = 0
        
        # 'required' est le nombre total de lettres de t qu'on doit encore trouver
        required = len(t)
        
        # On avance le pointeur de droite pour gonfler la fenêtre
        for right in range(len(s)):
            char_r = s[right]
            
            # Si cette lettre est requise (le compte est > 0), on diminue 'required'
            if char_count[ord(char_r)] > 0:
                required -= 1
                
            # On décrémente le compteur (même pour les lettres qui ne sont pas dans t,
            # elles deviendront négatives, ce qui nous aide à suivre l'excès)
            char_count[ord(char_r)] -= 1
            
            # Dès qu'on a trouvé toutes les lettres de t (required == 0)
            while required == 0:
                # Si la fenêtre actuelle est plus petite, on la sauvegarde
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # On essaie de rétrécir la fenêtre en bougeant le pointeur de gauche
                char_l = s[left]
                
                # On remet la lettre de gauche dans le tableau de compte
                char_count[ord(char_l)] += 1
                
                # Si cette lettre retirée était requise (le compte repasse au-dessus de 0),
                # on incrémente 'required', ce qui cassera la boucle while.
                if char_count[ord(char_l)] > 0:
                    required += 1
                    
                left += 1
                
        # On retourne la sous-chaîne si on a trouvé un min_len, sinon une chaîne vide
        return s[min_start : min_start + min_len] if min_len != float('inf') else ""
class Solution:
    def isValidSudoku(self, board) -> bool:
        # On crée 3 listes de 9 entiers (tous initialisés à 0)
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # On décale un "1" vers la gauche selon la valeur du chiffre
                # Exemple : si val == "3", bit devient 0000001000 (en binaire)
                bit = 1 << int(val)
                
                # Mathématique pour aplatir la grille 3x3 en un index de 0 à 8
                box_index = (r // 3) * 3 + (c // 3)

                # L'opérateur '&' vérifie si le bit est DÉJÀ allumé. 
                # Si oui, c'est un doublon !
                if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_index] & bit):
                    return False
                
                # L'opérateur '|=' allume le bit pour s'en souvenir pour la suite
                rows[r] |= bit
                cols[c] |= bit
                boxes[box_index] |= bit

        return True
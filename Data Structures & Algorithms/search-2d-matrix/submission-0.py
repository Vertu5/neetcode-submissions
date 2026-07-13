from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # --- ÉTAPE 1 : Recherche de la bonne ligne ---
        top = 0
        bottom = ROWS - 1
        
        while top <= bottom:
            row_mid = (top + bottom) // 2
            
            # Si la cible est plus petite que le début de la ligne, on cherche en haut
            if target < matrix[row_mid][0]:
                bottom = row_mid - 1
            # Si la cible est plus grande que la fin de la ligne, on cherche en bas
            elif target > matrix[row_mid][-1]:
                top = row_mid + 1
            # Sinon, la cible est forcément DANS cette ligne !
            else:
                break
                
        # Si on sort de la boucle sans avoir trouvé de ligne valide (les pointeurs se sont croisés)
        if top > bottom:
            return False
            
        # --- ÉTAPE 2 : Recherche dans la ligne trouvée ---
        # row_mid contient l'index de la bonne ligne grâce au "break"
        row_mid = (top + bottom) // 2
        left = 0
        right = COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == matrix[row_mid][mid]:
                return True
            elif target > matrix[row_mid][mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
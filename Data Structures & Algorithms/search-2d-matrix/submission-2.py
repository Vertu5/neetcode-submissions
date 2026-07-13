class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # Nos bornes pour un grand tableau imaginaire
        left = 0
        right = ROWS * COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # On traduit l'index 1D "mid" en coordonnées 2D
            row = mid // COLS
            col = mid % COLS
            
            valeur_milieu = matrix[row][col]
            
            # Recherche dichotomique classique
            if target == valeur_milieu:
                return True
            elif target > valeur_milieu:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
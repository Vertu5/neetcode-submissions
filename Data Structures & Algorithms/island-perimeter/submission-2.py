from typing import List

from typing import List

class Solution:

    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # O(1)
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)                                  # O(1)
        cols = len(grid[0])                               # O(1)

        total_perimeter = 0                               # O(1)
        
        for r in range(rows):                             # O(M) où M 
            for c in range(cols):                         # O(N) où N -> Total boucle: O(M * N)
                if grid[r][c] == 1:                       # O(1)
                    # On suppose que le bloc est seul
                    total_perimeter += 4                  # O(1)
                    
                    # On cherche les "amis" dans les 4 directions
                    for dr, dc in self.directions:             # O(1) car c'est toujours exactement 4 itérations
                        nr, nc = r + dr, c + dc           # O(1)
                        
                        # Si le voisin est dans la grille et que c'est un ami (terre)
                        check_b = 0 <= nr < rows and 0 <= nc < cols  # O(1)
                        if check_b and grid[nr][nc]:                 # O(1)
                            total_perimeter -= 1                     # O(1)
                    
        return total_perimeter                            # O(1)

# Time: O(M * N). Space: O(1).
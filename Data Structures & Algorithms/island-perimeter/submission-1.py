from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        total_perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # On suppose que le bloc est seul
                    total_perimeter += 4
                    
                    # On cherche les "amis" dans les 4 directions
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        
                        # Si le voisin est dans la grille et que c'est un ami (terre)
                        check_b = 0 <= nr < rows and 0 <= nc < cols
                        if check_b and grid[nr][nc]:
                            total_perimeter -= 1
                    
        return total_perimeter
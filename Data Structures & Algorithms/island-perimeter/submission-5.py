from typing import List, Tuple

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]      # O(1)
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.visited = set()

    def _find_start(self) -> Tuple[int, int]:
        """Trouve le premier bout de terre."""
        for r in range(self.rows):                                # O(M)
            for c in range(self.cols):                            # O(N)
                if self.grid[r][c] == 1:                          # O(1)
                    return r, c
        return -1, -1

    def _dfs_iterative(self, start_r: int, start_c: int) -> int:
        """Parcours DFS itératif (avec une pile/stack) qui applique la logique +4 / -1."""
        # On utilise une simple liste comme pile (Stack - LIFO)
        stack = [(start_r, start_c)]                              # O(1)
        self.visited.add((start_r, start_c))                      # O(1)
        
        total_perimeter = 0                                       # O(1)
        
        while stack:                                              # O(V) où V est la surface de l'île
            r, c = stack.pop()                                    # O(1) - On prend le DERNIER élément ajouté (DFS)
            
            # On suppose que le bloc est seul
            local_perimeter = 4                                   # O(1)
            
            for dr, dc in self.directions:                        # O(1)
                nr, nc = r + dr, c + dc                           # O(1)
                
                check_b = 0 <= nr < self.rows and 0 <= nc < self.cols # O(1)
                
                # Si le voisin est dans la grille et que c'est de la terre
                if check_b and self.grid[nr][nc] == 1:            # O(1)
                    
                    # 1. On retire 1 pour le bord partagé
                    local_perimeter -= 1                          # O(1)
                    
                    # 2. Si on ne l'a pas encore exploré, on le marque et l'ajoute à la pile
                    if (nr, nc) not in self.visited:              # O(1) en moyenne
                        self.visited.add((nr, nc))                # O(1)
                        stack.append((nr, nc))                    # O(1)
                        
            # On ajoute le périmètre local calculé au total
            total_perimeter += local_perimeter                    # O(1)
                
        return total_perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """Fonction principale."""
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        
        # 1. Trouver le point de départ
        start_r, start_c = self._find_start()
        
        # 2. Sécurité : si la grille ne contient que de l'eau
        if start_r == -1:
            return 0
            
        # 3. Lancer le calcul via le DFS itératif
        return self._dfs_iterative(start_r, start_c)

# Time Complexity: O(M * N) - Même chose que le BFS, on parcourt chaque case maximum une fois.
# Space Complexity: O(M * N) - Le set `visited` et le `stack` peuvent croître proportionnellement à la taille de l'île.
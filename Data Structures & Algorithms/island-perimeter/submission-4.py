from typing import List, Tuple
from collections import deque

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # O(1)
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.visited = set()

    def _find_start(self) -> Tuple[int, int]:
        """Trouve le premier bout de terre."""
        for r in range(self.rows):                                # O(M) où M est le nombre de lignes
            for c in range(self.cols):                            # O(N) où N est le nombre de colonnes
                if self.grid[r][c] == 1:                          # O(1)
                    return r, c
        return -1, -1

    def _bfs(self, start_r: int, start_c: int) -> int:
        """Parcours BFS itératif qui applique la logique +4 / -1."""
        queue = deque([(start_r, start_c)])                       # O(1)
        self.visited.add((start_r, start_c))                      # O(1)
        
        total_perimeter = 0                                       # O(1)
        
        while queue:                                              # O(V) où V est la surface de l'île (pire cas M*N)
            r, c = queue.popleft()                                # O(1)
            
            # On suppose que le bloc est seul
            local_perimeter = 4                                   # O(1)
            
            for dr, dc in self.directions:                        # O(1) car c'est toujours exactement 4 itérations
                nr, nc = r + dr, c + dc                           # O(1)
                
                check_b = 0 <= nr < self.rows and 0 <= nc < self.cols # O(1)
                
                # Si le voisin est dans la grille et que c'est un ami (terre)
                if check_b and self.grid[nr][nc] == 1:            # O(1)
                    
                    # 1. On retire 1 pour le bord partagé (même s'il a déjà été visité !)
                    local_perimeter -= 1                          # O(1)
                    
                    # 2. Si on ne l'a pas encore exploré, on le marque visité et on l'ajoute à la file
                    if (nr, nc) not in self.visited:              # O(1) en moyenne
                        self.visited.add((nr, nc))                # O(1) 
                        queue.append((nr, nc))                    # O(1)
                        
            # On ajoute le périmètre local au total une fois les 4 côtés vérifiés
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
            
        # 3. Lancer le calcul via BFS
        return self._bfs(start_r, start_c)

# Time Complexity: O(M * N) - On scanne la grille pour trouver le début, puis on visite l'île (au max M*N opérations).
# Space Complexity: O(M * N) - Dans le pire des cas, le set `visited` et la `queue` peuvent stocker toutes les cases de la grille.
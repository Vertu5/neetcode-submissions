from typing import List, Tuple

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # O(1)
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

    def _dfs(self, r: int, c: int) -> int:
        """Parcours DFS qui applique ta logique +4 / -1."""
        self.visited.add((r, c))                                  # O(1)
        
        # On suppose que ce bloc précis est seul
        local_perimeter = 4                                       # O(1)
        
        for dr, dc in self.directions:                            # O(1) (4 itérations fixes)
            nr, nc = r + dr, c + dc                               # O(1)
            
            check_b = 0 <= nr < self.rows and 0 <= nc < self.cols # O(1)
            
            # Si le voisin est dans la grille et que c'est un ami (terre)
            if check_b and self.grid[nr][nc] == 1:                # O(1)
                
                # 1. On retire 1 pour le bord partagé (même s'il a déjà été visité !)
                local_perimeter -= 1                              # O(1)
                
                # 2. Si on ne l'a pas encore exploré, on lance le DFS dessus
                if (nr, nc) not in self.visited:                  # O(1) en moyenne
                    local_perimeter += self._dfs(nr, nc)          # O(V) au total
                    
        return local_perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """Fonction principale."""
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        
        # 1. Trouver le point de départ
        start_r, start_c = self._find_start()
        
        # 2. Sécurité : si que de l'eau
        if start_r == -1:
            return 0
            
        # 3. Lancer le calcul
        return self._dfs(start_r, start_c)

# Time Complexity: O(M * N) - Dans le pire des cas, on visite tout pour trouver le début, puis l'île fait toute la grille.
# Space Complexity: O(M * N) - À cause du set `visited` et de la pile d'appels récursifs (call stack) du DFS.
class Solution:
    def __init__(self):
        self.direction = [(-1,0), (1,0), (0,1), (0,-1)]                 # O(1)
        self.visited = set()                                            # O(1)
        self.totalIsland = 0                                            # O(1)
        self.queue = deque()                                            # O(1)
        self.row_s = None                                               # O(1)
        self.col_s = None                                               # O(1)

    def numIslands(self, grid: List[List[str]]) -> int:                 # O(row_s * col_s)
        self.row_s = len(grid)                                          # O(1)
        self.col_s = len(grid[0])                                       # O(1)

        for r in range(self.row_s):                                     # O(row_s)
            for c in range(self.col_s):                                 # O(col_s)

                if grid[r][c] == "1" and (r,c) not in self.visited:     # O(1) on average 
                    self.totalIsland += 1                               # O(1)
                    self.visited.add((r,c))                             # O(1)

                    self.queue.append((r,c))                            # O(1)

                    self.bfs(grid) # or self dfs                            # 



        return self.totalIsland

    def bfs(self,grid):

        while self.queue:                                               # ??
            row, col = self.queue.popleft()                             # O(1)

            for dr, dc in self.direction:                               # O(1) 4 fixed direction 
                next_dr, next_dc = row + dr, col + dc
                check_b = 0 <= next_dr < self.row_s and 0 <= next_dc < self.col_s   # O(1)

                if check_b and  grid[next_dr][next_dc] == "1" and (next_dr, next_dc) not in self.visited:  # O(1)
                    self.visited.add((next_dr, next_dc))                # O(1)
                    self.queue.append((next_dr, next_dc))               # O(1)

    def dfs(self,grid):

        while self.queue:
            row, col = self.queue.pop()

            for dr, dc in self.direction:
                next_dr, next_dc = row + dr, col + dc
                check_b = 0 <= next_dr < self.row_s and 0 <= next_dc < self.col_s

                if check_b and  grid[next_dr][next_dc] == "1" and (next_dr, next_dc) not in self.visited:
                    self.visited.add((next_dr, next_dc))
                    self.queue.append((next_dr, next_dc))

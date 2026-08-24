class Solution:
    def __init__(self):
        self.direction = [(1,0),(0,1),(-1,0),(0,-1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_s = len(grid)
        col_s = len(grid[0])

        visited = set()
        global_area = 0

        for row in range(row_s):
            for col in range(col_s):

                if grid[row][col] == 1 and (row, col) not in visited: 
                    visited.add((row,col))
                    local_area = 1

                    # bfs or dfs I can put that on a function but that cool right now hahaha 
                    queue = deque([(row,col)])

                    while queue:

                        r, c = queue.popleft() # just delete left to do a dfs haha 

                        for dr, dc in self.direction:
                            next_r, next_c = r + dr, c + dc

                            check_b = 0 <= next_r < row_s and 0 <= next_c < col_s

                            if check_b and grid[next_r][next_c] and (next_r, next_c) not in visited: 
                                local_area += 1
                                visited.add((next_r, next_c))
                                queue.append((next_r, next_c))

                    global_area = max(local_area, global_area)

        return global_area

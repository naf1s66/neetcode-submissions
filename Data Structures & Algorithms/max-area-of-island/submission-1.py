class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        area = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def bfs(r, c):
            visit.add((r, c))
            current_area = 0
            q = collections.deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                current_area += 1
                directions = [
                    [1, 0],
                    [-1, 0],
                    [0, 1],
                    [0, -1],
                ]

                for dr, dc in directions:
                    if row + dr >= 0 and col + dc >= 0 and row + dr < rows and col + dc < cols and ((row + dr, col + dc)) not in visit and grid[row + dr][col + dc] == 1:
                        visit.add((row + dr, col + dc))
                        grid[row + dr][col + dc] = 0
                        q.append((row + dr, col + dc))
            return current_area


        for i in range(rows):
            for j in range(cols):
                if (( i, j)) not in visit and grid[i][j] == 1:
                    island_area = bfs(i, j)
                    area = max(area, island_area)

        
                

        return area

        


        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        fresh = 0
        minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        directions = [
                        [1, 0],
                        [-1, 0],
                        [0, 1],
                        [0, -1]
                    ]

        while q and fresh > 0:
            level_size = len(q)
            for size in range(level_size):

                row, col = q.popleft()
                    

                for dr, dc in directions:
                    if row + dr >= 0 and col + dc >= 0 and row + dr < rows and col + dc < cols and grid[row + dr][col + dc] == 1:
                        grid[row + dr][col + dc] = 2
                        fresh -= 1
                        q.append((row + dr, col + dc))
            minutes += 1

        if fresh > 0:
            return -1
        else:
            return minutes

        
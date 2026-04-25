class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num += 1
                    grid[i][j] = '0'
                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        row, col = queue.popleft()
                        directions = [
                            (1, 0),    
                            (-1, 0),   
                            (0, 1),    
                            (0, -1)    
                        ]
                        for dr, dc in directions:
                            new_row = row + dr
                            new_col = col + dc
                            if (
                                new_row >= 0 and
                                new_row < m and
                                new_col >= 0 and
                                new_col < n
                            ):
                                if grid[new_row][new_col] == '1':
                                    grid[new_row][new_col] = '0'
                                    queue.append((new_row, new_col))
        return num
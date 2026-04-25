class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        if image[sr][sc] == color:
            return image
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] != old_color:
                return
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        dfs(sr, sc)
        return image
            
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, 0, word, board):
                    return True
        
        return False
    
    def dfs(self, r: int, c: int, idx: int, word: str, grid: list[list[str]]) -> bool:
        if idx >= len(word):
            return True
        if self.is_out_of_bounds(grid, r, c) or word[idx] != grid[r][c]:
            return False
        
        temp = grid[r][c]
        grid[r][c] = "#"

        offsets = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        for r_offset, c_offset in offsets:
            if self.dfs(r + r_offset, c + c_offset, idx + 1, word, grid):
                return True
        
        grid[r][c] = temp

        return False

    def is_out_of_bounds(self, grid: list[list[str]], r: int, c: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        return r < 0 or r >= m or c < 0 or c >= n
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        left = 0
        top = 0
        right = n - 1
        bottom = m - 1

        while left <= right and top <= bottom:
            self.traverse_top(result, matrix, top, left, right + 1)
            top += 1
            self.traverse_right(result, matrix, top, right, bottom + 1)
            right -= 1
            if top <= bottom:
                self.traverse_bottom(result, matrix, bottom, right, left - 1)
                bottom -= 1
            if left <= right:
                self.traverse_left(result, matrix, bottom, left, top - 1)
                left += 1

        return result

    def traverse_top(
        self, 
        result: list[int], 
        matrix: list[list[int]], 
        r: int, 
        c: int, 
        stop: int
    ) -> None:
        for i in range(c, stop):
            result.append(matrix[r][i])
    
    def traverse_right(
        self, 
        result: list[int], 
        matrix: list[list[int]], 
        r: int, 
        c: int, 
        stop: int
    ) -> None:
        for i in range(r, stop):
            result.append(matrix[i][c])
    
    def traverse_bottom(
        self, 
        result: list[int], 
        matrix: list[list[int]], 
        r: int, 
        c: int, 
        stop: int
    ) -> None:
        for i in range(c, stop, -1):
            result.append(matrix[r][i])
    
    def traverse_left(
        self, 
        result: list[int], 
        matrix: list[list[int]], 
        r: int, 
        c: int, 
        stop: int
    ) -> None:
        for i in range(r, stop, -1):
            result.append(matrix[i][c])
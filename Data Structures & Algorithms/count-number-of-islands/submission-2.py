class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        disjoint_set = Disjoint_Set(grid)
        m, n = len(grid), len(grid[0])
        directions = [
            (0, 1),
            (1, 0)           
        ]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    coord1 = Coord(i, j)

                    for x, y in directions:
                        r, c = i + x, j + y
                        coord2 = Coord(r, c)
                        if coord2.is_in_bounds(m, n) and grid[r][c] == "1":
                            disjoint_set.union(coord1.get_elem(), coord2.get_elem())
        
        return disjoint_set.count
        
Elem = tuple[int, int]
class Info:
    def __init__(self, elem: Elem):
        self.root = elem
        self.rank = 1

class Coord:
    def __init__(self, x: int, y:int) -> None:
        self.x = x
        self.y = y
    
    def get_elem(self) -> Elem:
        return (self.x, self.y)
    
    def is_in_bounds(self, m: int, n: int) -> bool:
        return self.x >= 0 and self.x < m and self.y >= 0 and self.y < n

class Disjoint_Set:
    def __init__(self, grid: list[list[int]]) -> None:
        self._elements: dict[str, Info] = {}
        self.count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.add((i, j))

    def add(self, coord: Elem) -> None:
        if coord not in self._elements:
            self._elements[coord] = Info(coord)
            self.count += 1

    def find(self, elem: Elem) -> Elem | None:
        if elem not in self._elements:
            return None
        info = self._elements[elem]
        if info.root == elem:
            return elem
        info.root = self.find(info.root)

        return info.root
    
    def union(self, elem1: Elem, elem2: Elem) -> bool:
        root1, root2 = self.find(elem1), self.find(elem2)
        if not root1 or not root2 or root1 == root2:
            return False
        
        info1, info2 = self._elements[root1], self._elements[root2]

        if info1.rank >= info2.rank:
            info2.root = info1.root
            info1.rank += info2.rank
        else:
            info1.root = info2.root
            info2.rank += info1.rank

        self.count -= 1
        return True
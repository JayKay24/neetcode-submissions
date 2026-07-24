class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        if n == 1 and len(edges) == 0:
            return True
        
        adj_list = self.build_adj_list(n, edges)
        stack: list[tuple[int, int]] = []
        visited: set[int] = set()

        if len(edges) > 0:
            stack.append((edges[0][0], -1))
            visited.add(edges[0][0])

        while len(stack) > 0:
            current, parent = stack.pop()
            neighbors = adj_list[current]

            for neighbor in neighbors:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                stack.append((neighbor, current))
                visited.add(neighbor)
        
        if len(visited) != n:
            return False

        return True

    def build_adj_list(self, n: int, edges: list[list[int]]) -> dict[int, list[int]]:
        adj_list: dict[int, list[int]] = {}

        for i in range(n):
            adj_list[i] = []
        
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        return adj_list
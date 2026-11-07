class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]

        def has_path(start, target):
            stack = [start]
            visited = {start}

            while stack:
                node = stack.pop()

                if node == target:
                    return True

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            return False

        for a, b in edges:
            if has_path(a, b):
                return [a, b]

            graph[a].append(b)
            graph[b].append(a)
        
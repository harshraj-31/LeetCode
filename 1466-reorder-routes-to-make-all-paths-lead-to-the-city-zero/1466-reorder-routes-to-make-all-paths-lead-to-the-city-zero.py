class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Build the adjacency list
        adj = {i: [] for i in range(n)}
        
        for u, v in connections:
            adj[u].append((v, 1))  # Original direction requires reversal (cost 1)
            adj[v].append((u, 0))  # Artificial direction requires no reversal (cost 0)
            
        visited = set()
        reversals = 0
        
        def dfs(node):
            nonlocal reversals
            visited.add(node)
            
            for neighbor, cost in adj[node]:
                if neighbor not in visited:
                    reversals += cost
                    dfs(neighbor)
                    
        dfs(0)
        return reversals
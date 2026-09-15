class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        # Helper function to explore a whole province
        def dfs(city):
            for neighbor in range(n):
                # If there's a connection and we haven't visited this neighbor yet
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)  # Keep exploring from this new neighbor

        # Check every city
        for i in range(n):
            if i not in visited:
                # If we find an unvisited city, it means we found a new province!
                provinces += 1
                visited.add(i)
                # Explore all cities connected to this one
                dfs(i)
                
        return provinces
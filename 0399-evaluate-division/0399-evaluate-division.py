from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        # Step 1: Build the graph
        graph = defaultdict(dict)
        
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            value = values[i]
            
            # If A / B = 2.0, then an edge from A to B has weight 2.0
            graph[numerator][denominator] = value
            # The reverse edge from B to A has weight 1.0 / 2.0
            graph[denominator][numerator] = 1.0 / value
            
        # Step 2: Helper function to search for a path between two variables
        def dfs(current, target, visited):
            # If either variable doesn't exist in our graph, we can't evaluate it
            if current not in graph or target not in graph:
                return -1.0
                
            # If we found the target, the multiplier is 1.0
            if current == target:
                return 1.0
                
            # Mark as visited so we don't go in circles
            visited.add(current)
            
            # Explore all connected variables
            for neighbor, weight in graph[current].items():
                if neighbor not in visited:
                    # Recursively search from the neighbor to the target
                    result = dfs(neighbor, target, visited)
                    
                    # If the path was successful, multiply the weights together
                    if result != -1.0:
                        return weight * result
                        
            # If no valid path is found
            return -1.0
            
        # Step 3: Run DFS for every query
        answer = []
        for numerator, denominator in queries:
            # We pass a fresh empty set() for 'visited' on every new query
            answer.append(dfs(numerator, denominator, set()))
            
        return answer
"""
Given an origin and a destination in a directed graph in which edges can be blue or red, 
determine the length of the shortest path from the origin to the destination in which the 
edges traversed alternate in color. Return -1 if no such path exists.

Time Complexity: O(n*nlogn) where n is the number of nodes because once we make the graph, we have to loop through all the neighbors O(n)
but with every neighbor, we keep track of visited neighbors within that O(logn)

Space Complexity: O(V+E) where V is the number of nodes and E is the number of edges because we have to create the graph 
and create a set to keep track of all visited nodes

Data Structure: Graph
Algorithm: dfs
Time taken: Over 1 hour
"""
from collections import defaultdict

class Graph:
    links = defaultdict(list)
    
    def __init__(self):
        return
    
    def alternatingPath(self, origin, destination):
        # loop through links
        # create directed graph
        # keep track of the # of path to reach destination from each possible starting node, use dfs to backtrack
        # if # of path is < shortest_path, then replace
        
        # create neighbors that has a list of all their neighbor nodes + colors
        neighbors = defaultdict(list)
        for start, end, color in self.links:
            neighbors[start].append((end, color))
        
        shortestPath = -1
        # retrieving values in neighbors
        for neighbor in neighbors[origin]:
            # retrieving neighbors, color in neighbors[start]
            (node, color) = neighbor
            visited = set()
            visited.add(node)
            currCount = 1
            shortestPath = self.dfs(visited, node, color, neighbors, currCount, shortestPath, destination)
        return shortestPath


    def dfs(self, visited, start, color, neighbors, currCount, shortestPath, destination):
        visited.add(start)
        # return if we have reached destination
        if start == destination:
            if currCount < shortestPath or shortestPath == -1:
                shortestPath = currCount
                return shortestPath
        # skip paths that are either same color, or have already been to
        for neighborColor in neighbors[start]:
            (neighbor, c) = neighborColor
            if c == color or neighbor in visited:
                continue
            shortestPath = self.dfs(visited, neighbor, c, neighbors, currCount+1, shortestPath, destination)
        return shortestPath
    
def main():
    arr = [('A', 'B', "blue"), 
             ('A', 'C', "red"), 
             ('B', 'D', "blue"), 
             ('B', 'E', "blue"), 
             ('C', 'B', "red"), 
             ('D', 'C', "blue"), 
             ('A', 'D', "red"), 
             ('D', 'E', "red"), 
             ('E', 'C', "red")]
    graph = Graph()
    graph.links = arr
    print(graph.alternatingPath('A', 'E')) # Output: 4
    print(graph.alternatingPath('E', 'D')) # Output: -1

    return

main()
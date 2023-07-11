"""
Given an origin and a destination in a directed graph in which edges can be blue or red, 
determine the length of the shortest path from the origin to the destination in which the 
edges traversed alternate in color. Return -1 if no such path exists.

Time Complexity: 
    O(V+E) where V represents the number of verticies and E represents the number of edges in the graph
    This is because each node is visited once, and for each visited node, all its neighboring nodes are explored.
Space Complexity: 
    O(V+E) where V is the number of nodes and E is the number of edges because we have to create the graph
    which is proportional to the number of edges, the queue and set takes up O(V) space as every place will be added only once
Data Structure: Graph
Algorithm: bfs
Time taken: Over 1 hour
"""
from collections import defaultdict
from collections import deque
class Graph:
    links = defaultdict(list)
    
    def __init__(self):
        return
    
    def alternatingPath(self, origin, destination):
        # loop through links
        # create directed graph
        # keep track of the # of path to reach destination from each possible starting node, use dfs to backtrack
        # if # of path is < shortest_path, then replace
        graph = defaultdict(list)
        for start, end, color in self.links:
            graph[start].append((end, color))
            
        queue = deque([(origin, '', 0)])
        visited = set()
        while queue:
            current_node, current_color, path_length = queue.popleft()
            # Check if the current node is the destination
            if current_node == destination:
                return path_length
            # Explore neighbors of the current node
            for neighbor, neighbor_color in graph[current_node]:
                if neighbor_color != current_color:
                    if (neighbor, neighbor_color) not in visited:
                        visited.add((neighbor, neighbor_color, path_length+1))
                        queue.append((neighbor, neighbor_color, path_length+1))
        return -1
    
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
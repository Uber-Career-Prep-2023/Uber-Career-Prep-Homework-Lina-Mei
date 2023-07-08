""" 
Given an array of pairs of values representing edges in an unweighted graph, 
create the equivalent adjacency list/set representation 
(a map from element to a list or set of elements). Pairs represent directed edges: 
(A, B) means there is an edge from A to B. If the pair (B, A) is also provided then 
there is an undirected edge between A and B. For simplicity, you may assume that each 
node of the graph stores an integer rather than a generic data type and that the elements 
are distinct. Implement a basic DFS and BFS searching for a target value and a topological 
sort (using either DFS or Kahn’s algorithm).

Time complexities:
create - O(v) where v represents the number of total distinct nodes in the given list of nodes
bfs/dfs - O(v) where v represents the number of total distinct nodes in the given list of nodes
        because once we have traversed through a neighbor, we will not visit it again. Therefore the maximum
        number of times we visit a node is once.

Space complexities:
create - O(v+e) where v represents the number of total distinct nodes in the given list of nodes 
        and e represents a relation between two v's
bfs/dfs - O(v) at worst because at its worst case scenario, only one element is connected with all the other elements and therefore
        the queue will have to hold all the other elements all at once.
topologicalSort - 
"""

from collections import defaultdict


def create_graph(list_nodes):
    graph = defaultdict(list)
    for x, y in list_nodes:
        graph[x].append(y)
        if y not in graph:
            graph[y] = []
    return graph
        
def bfs(target, graph):
    result = "" # for testing
    traversed = set()
    root = list(graph.keys())[0]
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop()
        result = result + str(node)
        if node == target:
            return True
        for neighbors in graph[node]:
            if neighbors not in traversed:
                queue.append(neighbors)
        traversed.add(node)
    print(result)
    return False        
    
def dfs(target, graph):
    result = "" # for testing
    traversed = set()
    root = list(graph.keys())[0]
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result = result + str(node)
        if node == target:
            return True
        for neighbors in graph[node]:
            if neighbors not in traversed:
                stack.append(neighbors)
        traversed.add(node)
    print(result)
    return False    

def topologicalSort(graph):
    return dfs(graph.keys()[0],graph)

def main():
    print("test graph")
    list = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    graph = create_graph(list)
    print(graph)
    print("\ntest bfs")
    
    print(bfs(3, graph))
    print(bfs(20, graph))
    
    [print("\ntest dfs")]
    print(dfs(3, graph))
    print(dfs(20, graph))
    return
main()
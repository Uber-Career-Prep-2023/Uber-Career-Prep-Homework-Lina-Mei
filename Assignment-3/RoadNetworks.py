"""
In some states, it is not possible to drive between any two towns because they are not 
connected to the same road network. Given a list of towns and a list of pairs representing 
roads between towns, return the number of road networks. (For example, a state in which all 
towns are connected by roads has 1 road network, and a state in which none of the towns are 
connected by roads has 0 road networks.)

Time taken: 30 minutes
Time Complexity: O(nlogm) where m represents every town and n represents every network between two towns
    This is because the number of town that we have to traverse through reduces and we will have to go through every edge
    to form the graph
Space Complexity: O(m) because in our visited set, we have to store the # of towns
Data Structures: set
Algorithm: Dijkstra's algo

"""
from collections import defaultdict

def dfs(town, visited, neighbors):
    visited.add(town)
    for neighbor in neighbors[town]:
        if neighbor not in visited:
            dfs(neighbor, visited, neighbors)
    return

def roadNetworks(towns, roads):
    
    # make graph
    neighbors = defaultdict(list)

    for town1, town2 in roads:
        neighbors[town1].append(town2)
        neighbors[town2].append(town1)
        
    # given neighbors list, traverse each connected node using dfs, similar to dijkstra
    # mark town as visited
    visited = set()
    count = 0
    for town in neighbors:
        if town in visited:
            continue
        else:
            dfs(town, visited, neighbors)  
            count+=1      
    return count

def main():
    towns = ["Skagway", "Juneau", "Gustavus", "Homer", 
             "Port Alsworth", "Glacier Bay", "Fairbanks", 
             "McCarthy", "Copper Center", "Healy"]
    roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), 
             ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), 
             ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    
    print(roadNetworks(towns, roads)) # 2
    # (Networks are Gustavus-Glacier Bay and Anchorage-Fairbanks-McCarthy-Copper Center-Homer-Healy)
    
    towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"),
             ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    
    print(roadNetworks(towns2, roads2)) # 3? (Networks are Kona-Hilo-Volcano, 
    # Haiku-Kahului-Lahaina-Hana, and Lihue-Waimea-Princeville)

main()

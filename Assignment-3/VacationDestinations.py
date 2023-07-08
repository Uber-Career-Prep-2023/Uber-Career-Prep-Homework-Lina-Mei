"""
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly 
from each other with corresponding travel times in hours, return the number of destinations within k 
hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

Time Complexity: O(v) where n represents the number of neighbors the origin city is connected with, because once we traverse through the city,
                        we won't visit it again. therefore we only go through each city once.
Space Complexity: O(V+E) where V represents the number of cities in given list of inputs and E represents all the relations
Data Structure: queue
Algorithm: bfs
Time Taken: over 1 hour

"""
from collections import defaultdict, deque

# use heapq to always get shortest distance first

def createGraph(input):
    graph = defaultdict(list)
    for origin, destination, hour in input:
        graph[origin].append((destination, hour))
        graph[destination].append((origin, hour))
    return graph

def vacation(input, origin, k):
    graph = createGraph(input)
    visited = set()
    queue = deque([])
    count = 0
    queue.append((origin, -1))
    while queue:
        city, hours = queue.pop()
        visited.add(city)
        for neighbor, neighborHours in graph[city]:
            newHours = hours+neighborHours+1
            if newHours < k and neighbor not in visited:
                queue.append((neighbor, newHours))
                count+=1
            
    return count

def main():
    input = [("Boston", "New York", 4), 
             ("New York", "Philadelphia.", 2), 
             ("Boston", "Newport", 1.5), 
             ("Washington, D.C.", "Harper's Ferry", 1), 
             ("Boston", "Portland", 2.5), 
             ("Philadelphia", "Washington, D.C.", 2.5)]
    origin = 'New York'
    k = 5
    print(vacation(input, origin, k)) # 2
    k= 7
    print(vacation(input, origin, k)) # 4
    k=8
    print(vacation(input, origin, k)) # 6

    return

main()
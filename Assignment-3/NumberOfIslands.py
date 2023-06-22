""" 
Given a binary matrix in which 1s represent land and 0s represent water. 
Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).

Time Complexity: O(m*n)
Space Complexity: O(min(m*n))
Data Structure: 
Algorithm: DFS
Explanation:
The time complexity is O(m*n) where m is the # of rows and n is the # of cols because we have to traverse through
every number in the 2 by 2 matrix at least once.
The space complexity is O(min(m*n)) because the worse case scenario is if every [i][j] was a land, and we would have to
perform dfs on every [i][j].

25 minutes Total

Explanation:
"""
def dfs(grid, i, j):
    if grid[i][j] != 1:
        return
    grid[i][j] = 0
    if i+1 < len(grid):
        dfs(grid, i+1, j)
    if j+1 < len(grid[i]):
        dfs(grid, i, j+1)
    if i-1 >= 0:
        dfs(grid, i-1, j)
    if j-1 >= 0:
        dfs(grid, i, j-1)
    return

    
def NumberOfIsland(grid):
    count = 0
    if not grid:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                dfs(grid,i,j)
                count+=1
    return count

def main():
    grid = [[1,0,1,1,1],[1,1,0,1,1],[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,0]]
    print(NumberOfIsland(grid)) # 3
    grid2 = [[1,0,0],[0,0,0]]
    print(NumberOfIsland(grid2)) # 1
    return
main()
'''
Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.

Approach: dp
Time complexity:  O(N^2) where N represents the size of the matrix. We have to traverse every element in the matrix twice
Space complexity: O(N^2) where N represents the size of the matrix because we created another square matrix 
similiar to the given matrix
Time taken: 1 hr+

'''

def square(grid):
    dp = []
    size = len(grid)
    if grid is None or len(grid) < 1:
        return 0
    # start out with an identitcal grid with all 0's with 1 extra column and row to calculate last row and column
    dp = [[0]*(size+1) for _ in range(size+1)]
  
    #   check [col-1], [row-1] and [row-1][col-1]. if all conditions fulfil, do min of all those indexes + 1
    dim = 0

    for r in range(size):
        for c in range(size):
            if grid[r][c]:
                curr = dp[r][c]
                right = dp[r][c+1]
                bottom = dp[r+1][c]
                dp[r+1][c+1] = min(curr, bottom, right) + 1 # Be careful of the indexing since dp grid has additional row and column
                dim = max(dim, dp[r+1][c+1])
                
    return dim
        
    
input = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
print(square(input))
input2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]
print(square(input2))

'''
Boggle is a word game in which players compete to find the most words on a square grid of random letters. 
Valid words must be at least three characters and formed from non-overlapping (i.e., 
a position on the board can only be used once in a word) adjacent (including diagonal) letters. 
Given a Boggle board and a dictionary of valid words, return all valid words on the board.

Approach:
Trie + Backtracking DFS

Time complexity: O(L*N) where L represents the length of the word and N represents the # of words in the dictionary
Space Complexity: O(N*M+2K), where N is the number of words and M is the average length of the word and K represents 
the total number of elements in the board for the 2 sets.

Time Taken: 1hr+

'''

from Trie import TrieNode, Trie

    
def boggle(board, dictionary):
    trie = Trie()
    rows, cols = len(board), len(board[0])
    visited = set()
    result = set()
    
     # Create a trie of valid words
    for word in dictionary:
        trie.insert(word)
        
    def dfs(i, j, node, word):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) :
            return

        if board[i][j] not in node.children:
            return

        if (i, j) in visited:
            return

        word += board[i][j]
        node = node.children[board[i][j]]
        if node.validWord:
            result.add(word)
        visited.add((i, j))
        dfs(i, j+1, node, word)
        dfs(i-1, j+1, node, word)
        dfs(i+1, j+1, node, word)
        dfs(i, j-1, node, word)
        dfs(i-1, j-1, node, word)
        dfs(i+1, j-1, node, word)
        dfs(i-1, j, node, word)
        dfs(i+1, j, node, word)

        visited.remove((i, j))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.node, "")
    
    return result



dictionary = ["Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", 
"Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Rap", 
"Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"]

board = [
        ["A", "D", "E"],
        ["R", "C", "P"],
        ["L", "A", "Y"]
        ]

print("Boggle.py tests ")
print(boggle(board, dictionary))
 # Output: ['ACE', 'RAY', 'RAP', 'CAPE', 'CLAY', 'CLAP', 'PAY', 
#          'PACE', 'LAY', 'LACE', 'LAP', 'ACE', 'APE', 'YAP']

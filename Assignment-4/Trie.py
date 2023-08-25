'''
struct TrieNode {
   vector<struct TrieNode *> children; // a (resizable or fixed size) array of size 26
   bool validWord; // boolean to indicate if this node marks the end of a word
};

class Trie {
  struct TrieNode* root;

  void insert(string word); // adds a word to the trie
  bool isValidWord(string word); // returns a boolean indicating whether word is in the trie
  void remove(string word); // removes word, from the trie & deletes unused nodes
}

Time complexity:
Insert: O(L) where L represents the length of the word because you need to traverse down the trie level by level
Search: O(L) because you traverse down the trie along the characters of the word until you either 
find the entire word or determine that it doesn't exist in the trie.
Remove: O(L) because you check the children's nodes which can take up to O(L) time in the worst case, similar to the search operation.

Space complexity:
O(N*M), where N is the number of words and M is the average length of the word because we have to add every word to the dict and make
additional children from similar words that similiar beginning letters 

Time spent: 40 minutes
'''

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.validWord = False
        

class Trie:
    def __init__(self):
        self.node = TrieNode()
    
    def insert(self, word):
        curr = self.node
        for c in word:
            if c in curr.children:
                curr = curr.children[c] 
            else :
                newnode = TrieNode()
                curr.children[c] = newnode
                curr = newnode

        curr.validWord = True
                    
    def search(self, word):
            node = self.node
            for char in word:
                if node.children:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.validWord
                
        
    def remove(self, word):
        curr = self.node
        # is it the end of a word?
        if not curr.validWord:
            for ch in word:
                if curr.children:
                    if ch not in curr.children:
                        break
                    else:
                        curr = curr.children[ch]
            curr.validWord = False
                

# print("Trie.py tests ")
# test = Trie()   
# test.insert('hello')
# print(test.search('hello')) # true
# print(test.search('abc')) # false
# test.remove('hello')
# print(test.search('hello')) # false

        

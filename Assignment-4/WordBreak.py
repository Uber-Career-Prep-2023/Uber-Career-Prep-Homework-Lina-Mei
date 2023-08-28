'''
Given a string of characters without spaces and a dictionary of valid words, determine if it 
can be broken into a list of valid words by adding spaces. 

Approach: dp
Time complexity: O(N^2) where N is the number of characters in the input string. We have to traverse through 
all the characters at least twice to retrieve every possible substring
Space complexity: O(N) where N is the number of characters in the input string
Time taken: 40 mins
'''

def wordBreak(str, dict):
    lowercase_words = [word.lower() for word in dict]
    
    dp = [False]*(len(str)+1)
    dp[0] = True
    
    for i in range(1, len(str)+1):
        for j in range(i):
            # print(str[j:i])
            if dp[j] and str[j:i] in lowercase_words:
                dp[i] = True
                break
                
    return dp[-1]

dictionary = ["Elf", "Go", "Golf", "Man", "Manatee",
        "Not", "Note", "Pig", "Quip", "Tee", "Teen"]

print(wordBreak("mangolf", dictionary))         #true
print(wordBreak("manateenotelf", dictionary))   #true
print(wordBreak("quipig", dictionary))          #false


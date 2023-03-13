"""
Question 5: ShortestSubstring
Given a string and a second string representing required characters, return the length 
of the shortest substring containing all the required characters.

Time complexity: 
Space complexity: 

"""    

def ShortestSubstring(str1, str2):
    """ 
    :type str1 : string
    :type str2 : string
    :rtype length
    """
    # two pointer
    # use an array of tuples? to keep track
    # keep moving right pointer until at least 1 substring is achieved
    # when 1 has been found, move left pointer
    map = {}
    left = 0
    min = 0
    for i in range(len(str2)):
        map[str2] += 1
    for i in range(len(str1)):
        if len(map) == 0:
            min = i-left
        if str1[i] in map:
            if map[str1[i]] <= 1:
                map.pop(str1[i])
            else:
                map[str1[i]] -= 1
    return min

""" 
Examples:
Input Strings: "abracadabra", "abc"
Output: 4
(Shortest Substring: "brac")

Input Strings: "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx" (Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)
Output: 10
(Shortest Substring: "zzxwdcbxyz")

Input Strings: "dog", "god"
Output: 3
(Shortest Substring: "dog")

"""

# Spent 40 minutes
# this was really hard, wasn't sure where to begin
# wasn't sure when to update left pointer
# ended up looking at a solution
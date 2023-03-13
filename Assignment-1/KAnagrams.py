"""
Question 7: KAnagrams

Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k 
characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

Time complexity: O(n)
Space complexity: O(1)
assuming that both strings will only contain ASCII characters
"""
def KAnagrams(str1, str2, k):
    """ 
    :type str1 : string
    :type str2 : string
    :type num : int
    :rtype Boolean
    """
    # hash map?
    # iterate through the first string, add all characters into the hash map, map character -> # of occurence
    # iterate through the second string, check to see if every character is in the hash map (), decrease value if it is
    # if character is not in hash map, then increase our count variable by 1
    # check if our count variable is > num, if it is, then return false
    # finish traversing, return true if count is still <= num
    
    map = {}
    count = 0
    for i in range(len(str1)):
        character = str1[i].lower()
        if character in map:
            map[character] += 1
        else:
            map[character] = 1
    for i in range(len(str2)):
        character = str2[i].lower()
        if character in map:
            if map[character] > 0:
                map[character] -= 1
            else:
                count+=1;
                continue
        else:
            count+=1
    if count > k:
        return False

    return True

str1="apple"
str2="peach"
k=1
print(KAnagrams(str1,str2,k))

str1="apple"
str2="peach"
k=2
print(KAnagrams(str1,str2,k))

str1="cat"
str2="dog"
k=3
print(KAnagrams(str1,str2,k))

str1="debit curd"
str2="bad credit"
k=1
print(KAnagrams(str1,str2,k))

str1="baseball"
str2="basketball"
k=2
print(KAnagrams(str1,str2,k))
    
""" 
Examples:
Input Strings: "apple", "peach"
Input k: 1
Output: False

Input Strings: "apple", "peach"
Input k: 2
Output: True

Input Strings: "cat", "dog"
Input k: 3
Output: True

Input Strings: "debit curd", "bad credit"
Input k: 1
Output: True

Input Strings: "baseball", "basketball"
Input k: 2
Output: False


"""

# spent 21 minutes 33 seconds, wasn't sure why the last test case should be False instead of True?
# aren't you only adding the letters k and t, which means that it is at most 2 which should return true?
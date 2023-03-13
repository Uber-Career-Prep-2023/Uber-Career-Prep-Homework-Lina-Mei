"""
Question 2: ReverseVowels
Given a string, reverse the order of the vowels in the string.

Time complexity: O(n)
Space complexity: O(1)
Assuming that str will only have integers and there is a constraint on length of the string
"""

def ReverseVowels(str):
    """
    :type str: string 
    :rtype string
    """
    # iterate through string, store all the vowels in a queue
    # iterate through string again
    # check if its a vowel, if it is, do q.top()
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    queue = []
    output = ''
    for i in range(len(str)):
        if str[i].lower() in vowels:
            queue.append(str[i])
    # print(queue)  
    for i in range(len(str)):
        if str[i].lower() in vowels:
            output += queue.pop()
        else:
            output += str[i]
    
    return output       
            
str = "Uber Career Prep"
print(ReverseVowels(str))

str = "xyz"
print(ReverseVowels(str))

str = "flamingo"
print(ReverseVowels(str))
"""
    Input String: "Uber Career Prep"
    Modified String: "eber Ceraer PrUp"

    Input String: "xyz"
    Modified String: "xyz"

    Input String: "flamingo"
    Modified String: "flominga
"""

# spent 13 minutes 48 seconds
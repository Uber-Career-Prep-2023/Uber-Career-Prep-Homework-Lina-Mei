"""
Question 4: BackspaceStringCompare

Given two strings representing series of keystrokes, determine whether the resulting text is the same. 
Backspaces are represented by the '#' character so "x#" results in the empty string ("").

Time complexity: O(n)
Space complexity: O(1)

Assuming that the strings will only contain ASCII characters
Assuming that the # will only be used after ASCII characters are typed
"""    
def BackspaceStringCompare(str1, str2):
    """ 
    :type str1 : string
    :type str2: string
    :rtype boolean
    """
    # loop through first string, add to stack, if it's a #, remove from stack
    # same thing for second string
    # loop through first string, return false if they r not equal, otherwise true
    stack = []
    stack2 = []
    for i in range(len(str1)):
        if str1[i] == '#':
            if len(stack) > 0:
                stack.pop
        else:
            stack.append(str1[i].lower())
    for i in range(len(str2)):
        if str2[i] == '#':
            if len(stack2) > 0:
                print('ran')
                stack2.pop
        else:
            stack2.append(str2[i].lower())

    if len(stack) != len(stack2):  # Use len() to check length of stack and stack2
        return False
    while len(stack) > 0:
        s1 = stack.pop()
        s2 = stack2.pop()
        #print(s1)
        #print(s2)
        if s1 != s2:
            return False
    return True

str1 = "abcde"
str2 = "abcde"
print(BackspaceStringCompare(str1, str2))

str1 = 'Uber Career Prep'
str2 = 'u#Uber Careee#r Prep'
print(BackspaceStringCompare(str1, str2))

str1 = 'abcdef###xyz'
str2 = 'abcw#xyz'
print(BackspaceStringCompare(str1, str2))

str1 = 'abcdef###xyz'
str2 = 'abcdefxyz###'
print(BackspaceStringCompare(str1, str2))
"""
Examples:
eInput Strings: "abcde", "abcde"
Output: True

Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
Output: True

Input Strings: "abcdef###xyz", "abcw#xyz"
Output: True

Input Strings: "abcdef###xyz", "abcdefxyz###"
Output: False 

"""

# spent 40 minutes
# Wasn't able to get it

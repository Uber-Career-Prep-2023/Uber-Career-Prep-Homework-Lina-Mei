"""
Given a string, return the string with the order of the space-separated words reversed

Time taken: 20 minutes
Time Complexity: O(n) where n is the number of words separated because we have to reverse all the words,
requiring a traversal through all of them
Space Complexity: O(1) only local string variables are used
Data Structure: 
Algorithm: 


"""

def reverseWords(str):
    str_arr = str.strip().split(" ")
    str_arr.reverse()
    result = ' '.join(str_arr)
    return result

def main():
    input = "Uber Career Prep" #"Prep Career Uber"
    print(reverseWords(input))
    input2 = "Emma lives in Brooklyn, New York." #"York. New Brooklyn, in lives Emma"
    print(reverseWords(input2))

    return

main()

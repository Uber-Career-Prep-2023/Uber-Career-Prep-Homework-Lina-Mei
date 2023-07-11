"""
Given a string, return the string with the order of the space-separated words reversed

Time taken: 20 minutes
Time Complexity: 
    O(n) where n is the number of characters in the string
Space Complexity: 
    O(n) array where n represents the # of words in the string because we have to store every word
Data Structure: Array
Algorithm: 

"""
def reverseWords(str):
    # Go through string, add word to an array
    # edge case: if there are no more characters after
    words = []
    current_word = ""
    
    # append word if there is a space
    for char in str:
        if char == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    if current_word != "":
        words.append(current_word)
        
    # go through array in reverse
    reversed_words = " ".join(words[::-1])
    return reversed_words

def main():
    input = "Uber Career Prep" #"Prep Career Uber"
    print(reverseWords(input))
    input2 = "Emma lives in Brooklyn, New York." #"York. New Brooklyn, in lives Emma"
    print(reverseWords(input2))

    return

main()

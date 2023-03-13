"""
Question 8: MergeIntervals
Given a list of integer pairs representing the low and high end of an interval, inclusive, 
return a list in which overlapping intervals are merged.


Time complexity: 
Space complexity: 

Assuming that are no negative integers

"""

def MergeIntervals(list_int):
    """ 
    :type : List[List[int]
    """
    
    # rearrange list into starts and ends array
    # sort arrays
    starts = []
    ends = []
    results = []
    for pairs in list_int:
        starts.append(pairs[0])
        ends.append(pairs[1])
    starts.sort
    ends.sort
    
    start = starts[0]
    end = ends[0]
    for i in range(len(starts)):
        if ends[i] < starts[i+1]:
            start = starts[i+1]
        end = ends[i+1]    
    
    return results
    
list_int =  [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
print(MergeIntervals(list_int))
    
list_int =  [(5, 8), (6, 10), (2, 4), (3, 6)]
print(MergeIntervals(list_int))
    
list_int = [(10, 12), (5, 6), (7, 9), (1, 3)]
print(MergeIntervals(list_int))
    
""" 
Examples:

Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
Output: [(4, 8), (1, 3), (9, 12)]

Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
Output: [(2, 10)]

Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
Output: [(10, 12), (5, 6), (7, 9), (1, 3)]

"""
# Spent 40 minutes
# this one was really hard, I wasn't even sure where to start
# ended up looking up a solution

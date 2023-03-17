"""
Question 8: MergeIntervals
Given a list of integer pairs representing the low and high end of an interval, inclusive, 
return a list in which overlapping intervals are merged.


Time complexity: O(nlogn)
Space complexity: o(n)

Assuming that are no negative integers

"""

def MergeIntervals(intervals):
    """ 
    :type : List[List[int]]
    """
    
    # rearrange list into starts and ends array
    # sort arrays
    intervals.sort(key = lambda i : i[0])   # sort all the intervals by the first element
    output = list([intervals[0]])           # first interval
    for start, end in intervals[1:]:
        prev_End = intervals[-1][1]
        if start <= prev_End:               # have to merge
            output[-1][1] = max(prev_End, end)
        else:
            output.append([start, end])     # don't merge
    
    return output
    
intervals =  [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
print(MergeIntervals(intervals))
    
intervals =  [(5, 8), (6, 10), (2, 4), (3, 6)]
print(MergeIntervals(intervals))
    
intervals = [(10, 12), (5, 6), (7, 9), (1, 3)]
print(MergeIntervals(intervals))
    
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
# ended up looking up a solution, but I cannot edit it because it's a tuple, how to go around this issue?

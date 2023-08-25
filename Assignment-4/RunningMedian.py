'''
You will be given a stream of numbers, one by one. After each new number, return the median of the numbers so far.

Examples (newest number at each step in bold):
Input: 1
Output: 1

Input: 1, 11
Output: 6

Input: 1, 11, 4
Output: 4

Input: 1, 11, 4, 15
Output: 7.5

Input: 1, 11, 4, 15, 12
Output: 11


Approach: Maintain two heaps
Time complexity: O(Nlogn) where N represents the total elements in the heaps because at its worst case, 
we have to traverse through all elements of the heap and inserting elements into the heap takes O(logN) time
Space complexity: O(N) where N represents the total elements in the heaps. Min and max heap would contain N/2 elements.
Time taken: 50 minutes
'''
import heapq
class Median():
    
    def __init__(self) -> None:
        self.min = []
        self.max = []
        
        
    def runningMedian(self, num):
        if not self.max or num <= -self.max[0]:
            heapq.heappush(self.max, -num)
        else:
            heapq.heappush(self.min, num)

        # Balance the heaps
        if len(self.max) > len(self.min) + 1:
            heapq.heappush(self.min, -heapq.heappop(self.max))
        elif len(self.min) > len(self.max):
            heapq.heappush(self.max, -heapq.heappop(self.min))
            
        if len(self.max) == len(self.min):
            return (-self.max[0] + self.min[0]) / 2.0
        else:
            return -self.max[0]

        
output = Median()
print(output.runningMedian(1)) # 1
print(output.runningMedian(11)) # 6
print(output.runningMedian(4)) # 4
print(output.runningMedian(15)) # 7.5
print(output.runningMedian(12)) # 11
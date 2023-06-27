""" 
Given a number, k, return an array of the first k binary numbers, represented as strings.

30 minutes Total
Time complexity: O(n*logn)
Space complexity: O(n)

Explanation: 
O(n*logn) time complexity where n represents k ->  We have to do convert maximum k times, and for every conversion
when we use the built-in python function, k gets divided by 2 in order to retrieve the binary value.
O(n) space complexity where n represents k -> we have to store k number of elements in the output array

Data Structure: N/a
Algorithm: N/a

Assumptions: That k is non-negative
"""

def firstKBinaryNumbers(k):
    # Python built in function bin()
    output = []
    for i in range(k):
        output.append(str(bin(i)[2:]))
    return output

def main():
    num = 5
    print(firstKBinaryNumbers(num)) # ["0", "1", "10", "11", "100"]
    num2 = 10
    print(firstKBinaryNumbers(num2)) # "0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
    return
main()
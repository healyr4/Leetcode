# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    # Shift A k times
    
    # Need to check for edge case if array is empty...
    
    length = len(A)
    K = K% length

    shifted = A[-K:] + A[:-K]

    return shifted

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # A = numbers on Tape
    # N integers
    # P = integer which splits tape
    # min_difference = abs(sum) of diff between two parts
    min_distance = 10000000000000000
    temp_distance = 0
    sum_left = 0
    sum_right = sum(A)
    for i in range(1, len(A)):
        sum_left+= A[i-1]
        sum_right-= A[i-1]
        abs_diff = abs(sum_left-sum_right)

        if abs_diff < min_distance:
            min_distance = abs_diff
    return min_distance

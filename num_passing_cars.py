# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # N = num cars
    # p = 0 east
    # q = 1 west
    # p must be less than q
    num_passing = 0
    limit= 1* 10**9
    n = len(A)
    num_zeros = A.count(0)
    num_ones = n - num_zeros


    if (n ==1):
        return 0
    for index, val in enumerate(A):
        if val == 0:
            num_zeros -= 1
            num_passing += 1*num_ones
        else:
            num_ones -=1
        if num_passing > limit:
            return -1
    return num_passing

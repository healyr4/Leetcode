# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    set_a = set(A)
    max_num = max(set_a)
    if (max_num < 1):
        return 1

    for num in range(1, max_num+2):
        if num not in set_a:
            return num

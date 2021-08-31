# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # First convert num to binary
    binary_num = bin(N)
    print(type(binary_num))
    my_binary = toBinary(N)
    xs = my_binary.strip('0').split('1')
    print(xs)
    return max([len(x) for x in xs])


def toBinary(num):
    binary = ''
    while num!=0:
        quotient = num%2
        binary+= str(quotient)
        num = num//2

    return binary[::-1]

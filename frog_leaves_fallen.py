# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):

    #Create array for all leaves
    leaf_fallen= [False] * X
    counter = 0
    flag = -1
    for index, value in enumerate(A):
        #If leaf hasn't fallen yet
        # Mark that it has now fallen
        
        if(not(leaf_fallen[value-1])):
            leaf_fallen[value-1] = True
            counter += 1
            if counter == X:
                return index
    return flag
    

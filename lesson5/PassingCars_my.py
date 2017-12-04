def solution(A):
    zeros = 0
    pCars = 0
    for i in range(0,len(A)):
        if A[i] == 0:
            zeros += 1
        else:
            pCars += zeros
        
        if pCars > 1000000000:
            return -1
    return pCars

def solution(A):
    A = sorted(A)
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2] and A[i] + A[i+2] > A[i+1] and A[i+2] + A[i+1] > A[i]:
            return 1    
    return 0

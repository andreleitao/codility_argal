def solution(X, A):
    leaves = [0] * 1000010
    total = ((1+X)*X)/2
    
    if len(A) == 1:
        if A[0] == 1:
            return 0
        else:
            return -1
            
    for idx in range(len(A)):
        if leaves[A[idx]] == 0:
            leaves[A[idx]] = 1
            total -= A[idx]
            if total == 0:
                return idx
    return -1

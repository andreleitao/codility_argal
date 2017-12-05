# Correctness: 40% Performance: 60%

def solution(A):
    # write your code in Python 3.6
    P = prefix_sums(A)
    
    min_average = 10000
    idx_min_average = 0
    for idx in range(len(A)-1):
        diff = count_total(P,idx,idx+1)
        if diff < min_average:
            min_average = diff
            idx_min_average = idx
        
    return idx_min_average

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P
    
def count_total(P, x, y):
    return P[y + 1] - P[x]

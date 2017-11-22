def solution(A):
    xor_result = 0
    for idx in range(len(A)):
        xor_result ^= (idx+1) ^ A[idx]
        
    if xor_result == 0:
        return 1
    return 0

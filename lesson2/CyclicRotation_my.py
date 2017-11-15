def solution(A, K):
    length = len(A)
    rot = [0] * length
    for idx in range(length):
        new_idx = idx+K
        if new_idx <= length-1:
            rot[new_idx] = A[idx]
        else:
            rot[new_idx%length] = A[idx]
            
    return rot

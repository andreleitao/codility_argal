def solution(A):
    if len(A) == 3: return A[0] * A[1] * A[2]
    
    A.sort()

    neg = []
    pos = []
    for a in A:
        if a <= 0:
            neg.append(a)
        elif a > 0:
            pos.append(a)
            
    max_neg = -1000000001    
    max_pos = -1000000001
    
    if len(neg) >= 2 and len(pos) > 0:
        max_neg = neg[0] * neg[1] * pos[-1]
    elif len(pos) == 0:
        max_neg = neg[-1] * neg[-2] * neg[-3]    
    if len(pos) >= 3:
        max_pos = pos[-1] * pos[-2] * pos[-3]
    
    return max_neg if max_neg >= max_pos else max_pos

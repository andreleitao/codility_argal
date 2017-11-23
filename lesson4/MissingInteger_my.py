def solution(A):
    ordered = set(A)
    for idx in range(len(A)):
        if idx+1 not in ordered:
            return idx+1
    return len(A)+1

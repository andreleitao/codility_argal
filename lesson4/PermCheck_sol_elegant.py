def solution(A):
    if set(A) == set(range(1, 1+len(A))):
        return 1
    else:
        return 0

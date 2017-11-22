def solution(A):
    A = sorted(A)
    if A == range(1,len(A)+1):
        return 1
    else:
        return 0

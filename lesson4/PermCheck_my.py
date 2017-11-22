def solution(A):
    found = [0] * len(A)
    max_a = 0
    for a in A:
        if not 1 <= a <= len(A):
            return 0
            
        if found[a-1] == 0:
            found[a-1] = 1
        else:
            return 0

    return 1

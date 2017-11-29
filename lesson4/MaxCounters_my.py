def solution(N, A):
    counters = [0] * N
    max_count = 0
    for idx in range(len(A)):
        if A[idx] >= 1 and A[idx] <= N:
            counters[A[idx]-1] += 1            
            max_count = max(max_count, counters[A[idx]-1])
        elif A[idx] == N + 1:
            counters = [max_count] * N
    return counters

def solution(N, A):
    counters = [0] * N
    max_val = 0
    current_max = 0
    for v in A:
        if 1 <= v <= N:
            if max_val > counters[v-1]:
                counters[v-1] = max_val
            counters[v-1] += 1
            if current_max < counters[v-1]:
                current_max = counters[v-1]
        else:
            max_val = current_max
 
    counters = [max(max_val,i) for i in counters]
 
    return counters

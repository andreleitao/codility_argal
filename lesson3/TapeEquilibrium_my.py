def solution(A):
    sums = []
    total = 0
    last = len(A)-1
    
    for index in range(last):
        total += A[index]    
        sums.append(total)
    total += A[last] 
        
    min_diff = 10000
    for sum in sums:
        min_diff = min(min_diff, abs(sum - (total-sum)))
        
    return min_diff

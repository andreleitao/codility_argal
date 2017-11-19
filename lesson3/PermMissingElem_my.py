def solution(A):    
    count = 0
    count_sum = 0
    sum = 0
    for a in A:
        sum += a
        count += 1
        count_sum += count
        
    return count_sum + len(A) + 1 - sum

# lesson 1 BinaryGap 

def solution(N):
    rest = []
    while N > 1:
        rest.append(N%2)
        N = N/2
    rest.append(1)
    
    if (len(rest) < 3):
        return 0
    else:            
        # binary = list(reversed(rest))
        binary = rest[::-1]
    
        max_count = 0
        count = 0
        for digit in binary:
            if digit == 0:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        
        return max_count

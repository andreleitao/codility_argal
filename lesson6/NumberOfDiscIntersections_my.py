100% 0%
def solution(A):
    l = len(A)
    reaches = [] * l
 
    for i in range(l):
        values = [i-A[i], i+A[i]]
        reaches.append(values)
        
    count = 0
    l = len(reaches)
    for i in range(l):
        for j in range(i+1, l):
            first = reaches[i][0] >= reaches[j][0] and reaches[i][0] <= reaches[j][1]
            second = reaches[i][1] >= reaches[j][0] and reaches[i][1] <= reaches[j][1]
            third = reaches[j][0] >= reaches[i][0] and reaches[j][0] <= reaches[i][1]
            forth = reaches[j][1] >= reaches[i][0] and reaches[j][1] <= reaches[i][1]
            if first or second or third or forth:
                count += 1
                if count == 10000000:
                    return -1
        
    return count

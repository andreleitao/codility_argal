# OddOccurrencesInArray
# Find value that occurs in odd number of elements.
# Correctness 100% Performance 25% = 66%

def solution(A):
    found = [0] * 10000000
    
    for e in A:
        if found[e] == e:
            found[e] = 0
        else:
            found[e] = e
        
    elements = filter(lambda a: a != 0, found)
    
    return elements.pop()

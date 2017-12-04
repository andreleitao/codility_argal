// Copied from https://codesays.com/2014/solution-to-count-div-by-codility/
def solution(A, B, K):
    if A % K == 0:  
	return (B - A) // K + 1
    else:
        return (B - (A - A % K )) // K

def solution(S, P, Q):
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        
    next_nucl = [[-1]*len(S), [-1]*len(S), [-1]*len(S), [-1]*len(S)]
    next_nucl[mapping[S[-1]] - 1][-1] = len(S)-1
    for index in range(len(S)-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index    
    
    answers = []
    for i in range(len(P)):
        begin = P[i]
        end = Q[i]
        if next_nucl[0][begin] <= end and next_nucl[0][begin] != -1:
            answers.append(1)
        elif next_nucl[1][begin] <= end and next_nucl[1][begin] != -1:
            answers.append(2)
        elif next_nucl[2][begin] <= end and next_nucl[2][begin] != -1:
            answers.append(3)
        else:
            answers.append(4)
    
    return answers

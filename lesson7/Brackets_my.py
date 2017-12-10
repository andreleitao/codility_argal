66% 20%
def solution(S):
    if len(S) == 0:
        return 1
    else:
        mapping = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        chars = list(S)
        
        size = len(chars)
        if size % 2 != 0:
            return 0
        else:            
            # print(chars)
            while len(chars) > 0:
                if chars[0] in mapping:
                    return 0
                else:
                    changing = True
                    while len(chars) > 0 and changing:
                        changing = False
                        if chars[1] in mapping:
                            if chars[0] == mapping[chars[1]]:
                                chars = chars[2:]
                                changing = True
                                # print(chars)
                        
                        if len(chars) > 0:
                            if chars[-1] in mapping:
                                if chars[-2] == mapping[chars[-1]]:
                                    chars = chars[:-2]
                                    changing = True
                                    # print(chars)
                    
                    if len(chars) > 0:
                        tail = chars.pop()
                        if tail not in mapping:
                            return 0
                        else :
                            if chars[0] != mapping[tail]:
                                return 0
                            else:
                                chars = chars[1:]
                
                # print(chars)
                
    return 1

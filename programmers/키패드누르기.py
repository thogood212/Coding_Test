from collections import deque

def solution(numbers, hand):
    answer = ''
    last_L = 10
    last_R = 12
    result = []
    
    address = [[i,j] for i in range(4) for j in range(3)]
    
    numbers= deque(numbers)
    while numbers:
        p = numbers.popleft()
        if p==0:
            p = 11
        if p in [1,4,7]:
            result.append('L')
            last_L = p
        elif p in [3,6,9]:
            result.append('R')
            last_R = p
        else:
            L = address[last_L-1]
            R = address[last_R-1]
            P = address[p-1]
            length_L = abs(L[0]-P[0])+abs(L[1]-P[1])
            length_R = abs(R[0]-P[0])+abs(R[1]-P[1])
            if length_L==length_R:
                if hand=='left':
                    result.append('L')
                    last_L = p
                else:
                    result.append('R')
                    last_R = p
            elif length_L>length_R:
                result.append('R')
                last_R = p
            else:
                result.append('L')
                last_L = p
    
    answer= ''.join(result)
    return answer
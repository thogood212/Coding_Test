import heapq

def solution(k, score):
    answer = []
    q = []
    Maxlast = 0
    for s in score:
        heapq.heappush(q,s)        
        if len(q)>=k:
            last = heapq.heappop(q)
            Maxlast=max(last,Maxlast)
            answer.append(Maxlast)
        else:
            last = heapq.heappop(q)
            answer.append(last)
            Maxlast=min(last,Maxlast)
            heapq.heappush(q,last) 
    return answer
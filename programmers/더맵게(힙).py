import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for socv in scoville:
        heapq.heappush(heap,socv)
        
    while heap[0] < K:
        h1 = heapq.heappop(heap)
        h2 = heapq.heappop(heap)     
        if h1 < K :
            heapq.heappush(heap, h1+(h2*2))
            answer+=1

        if len(heap)<=1 and h1+(h2*2)<K:
            return -1 
    return answer
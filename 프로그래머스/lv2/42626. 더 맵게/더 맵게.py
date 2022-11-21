from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while True:
        first = heappop(scoville)
        if first >= K:
            break
            
        if len(scoville) == 0:
            return -1
        
        answer+=1
        heappush(scoville, first + (heappop(scoville)*2))

    return answer
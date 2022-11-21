from heapq import heappop,heappush,heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while True:
        first = heappop(scoville)
        if first >= K:
            break
            
        elif len(scoville) == 0:
            return -1
        
        heappush(scoville,first + (heappop(scoville) * 2))
        answer += 1
        
    return answer
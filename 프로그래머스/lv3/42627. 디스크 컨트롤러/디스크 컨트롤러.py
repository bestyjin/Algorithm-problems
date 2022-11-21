from heapq import  heappop, heappush
def solution(jobs):
    answer, start, now, i = 0, -1, 0, 0
    heap=[]
    
    while i < len(jobs):
        for j in jobs:
            if start< j[0] <=now:
                heappush(heap,[j[1],j[0]])
        
        if len(heap) > 0:
            current = heappop(heap)
            start = now
            now += current[0]
            answer+=now-current[1]
            i+=1
        else:
            now+=1
        

    return answer//len(jobs)
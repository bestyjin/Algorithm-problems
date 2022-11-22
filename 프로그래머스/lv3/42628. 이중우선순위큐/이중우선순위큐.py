from heapq import heappush,heappop,nlargest
def solution(operations):
    heap=[]
    for o in operations:
        command, num = o.split()
        if command == 'I':
            heappush(heap,int(num))
        elif command == 'D':
            if len(heap) == 0:
                continue
            if num == '1':
                heap.remove(max(heap))
            elif num == "-1":
                heappop(heap)
    
    if len(heap) == 0:
        return [0,0]
    else:
        return [max(heap),heappop(heap)]

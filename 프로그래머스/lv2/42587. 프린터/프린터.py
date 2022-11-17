from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i,p in enumerate(priorities):
        queue.append((i,p))
    
    
    while True:
        j = queue.popleft()
        if any(j[1] < q[1] for q in queue):
            queue.append(j)
        else:
            answer+=1
            if j[0] == location:
                break
    return answer
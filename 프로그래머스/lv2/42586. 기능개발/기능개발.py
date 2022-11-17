import math
def solution(progresses, speeds):
    answer = []
    stack = []
    for p,s in zip(progresses,speeds):
        day = math.ceil((100-p)/s)
        if len(stack)==0 or stack[0] >= day:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack=[]
            stack.append(day)
            
    answer.append(len(stack))

    return answer
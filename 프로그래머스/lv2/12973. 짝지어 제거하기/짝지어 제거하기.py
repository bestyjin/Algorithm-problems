def solution(s):
    stack=[]
    for i,n in enumerate(s):
        if len(stack)==0:
            stack.append(n)
        else:
            if n == stack[-1]:
                stack.pop()
            else:
                stack.append(n)
    if len(stack) == 0:
        return 1
    else:
        return 0
            
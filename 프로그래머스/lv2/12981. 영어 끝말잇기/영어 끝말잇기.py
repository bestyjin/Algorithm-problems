def solution(n, words):
    stack = []
    for i,w in enumerate(words):
        if len(stack)!=0 and (stack[-1][-1] != w[0] or stack.count(w)>0):
            return [i%n+1, i//n+1]
        stack.append(w)
                    
    return [0,0]
            
def solution(n):
    answer = 0
    next_n = n+1
    while n<next_n:
        if bin(n)[2:].count('1') == bin(next_n)[2:].count('1'):
            return next_n
        next_n+=1
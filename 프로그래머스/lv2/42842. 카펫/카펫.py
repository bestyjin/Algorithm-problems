def solution(brown, yellow):
    total = brown+yellow    # total 격자 전체 개수 (카펫 넓이)
    
    for a in range(1,total+1):
        if total % a==0:
            b = total//a
            if a >= b and 2*a+2*b-4 == brown:
                return [a,b]
                
    
    
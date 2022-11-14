def solution(clothes):
    answer = 1
    hash_clothes=dict()
    for _, t in clothes:
        if t not in hash_clothes:
            hash_clothes[t]=2
        else:
            hash_clothes[t]+=1
    
    for value in hash_clothes.values():
        answer *= value
        
    return answer-1
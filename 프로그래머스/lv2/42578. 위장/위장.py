def solution(clothes):
    answer = 1
    hash_clothes = dict()
    for c in clothes:
        if c[1] in hash_clothes:
            hash_clothes[c[1]]+=1
        else:
            hash_clothes[c[1]]=2
    
    for val in hash_clothes.values():
        answer*=val
    
    return answer-1
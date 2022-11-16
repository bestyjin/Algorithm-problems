def solution(genres, plays):
    answer = []
    hash_genres={}
    hash_plays={}
    
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g not in hash_genres:
            hash_genres[g]=p
        else:
            hash_genres[g]+=p
            
        if g not in hash_plays:
            hash_plays[g]=[(i,p)]
        else:
            hash_plays[g].append((i,p))
            
    for (k,v) in sorted(hash_genres.items(), key= lambda x:x[1], reverse=True):
        for (i,p) in sorted(hash_plays[k], key= lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
            
        
    return answer
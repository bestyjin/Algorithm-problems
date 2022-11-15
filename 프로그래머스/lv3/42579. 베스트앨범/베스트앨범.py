def solution(genres, plays):
    answer = []    
    hash_genre = dict()
    hash_play = dict()
    
    for i, (g,p) in enumerate(zip(genres,plays)):
        if g in hash_genre:
            hash_genre[g] += p
        else:
            hash_genre[g] = p
            
        if g in hash_play:
            hash_play[g].append((i,p))
        else:
            hash_play[g]=[(i,p)]
    
    for j in dict(sorted(hash_genre.items(), key=lambda x: x[1], reverse=True)):
        for k in sorted(hash_play[j], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(k[0])
    
    return answer
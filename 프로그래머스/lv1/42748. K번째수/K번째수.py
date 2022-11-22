def solution(array, commands):
    answer = []
    array2=[]
    for c in commands:
        array2=array[c[0]-1:c[1]]
        array2.sort()
        answer.append(array2[c[2]-1])
    
    return answer
def solution(numbers, direction):
    answer = []
    start=0
    end=0
    
    if direction == "right":
        answer.append(numbers[-1])
        for n in range(len(numbers)-1):
            answer.append(numbers[n])
    elif direction == "left":
        for n in range(1,len(numbers)):
            answer.append(numbers[n])
        answer.append(numbers[0])
    return answer
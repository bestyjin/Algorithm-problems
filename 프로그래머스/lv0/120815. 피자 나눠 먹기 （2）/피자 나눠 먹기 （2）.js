function solution(n) {
    var answer = 1;
    while (true){
        if((answer*6)%n===0){
            return answer;
        }
        answer+=1;
    }
    return answer;
}
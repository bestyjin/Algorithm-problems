function solution(n) {
    var answer = 0;
    for(let i=1; i<n+1; i++){
        if(n%i==0){
            answer+=1;
        }
    }
    return answer;
}
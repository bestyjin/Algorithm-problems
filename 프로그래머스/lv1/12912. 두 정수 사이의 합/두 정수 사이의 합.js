function solution(a, b) {
    let answer=0;
    if(a>b){
        for(let i = b; i<=a; i+=1) {
            answer+=i;
        }
    } else {
        for(let i = a; i<=b; i+=1) {
            answer+=i;
        }
    }
    return answer;
}
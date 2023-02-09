function solution(n) {
    let answer = [];
    n = String(n).split('');
    
    for (let i = n.length-1; i >= 0; i-=1){
        answer.push(Number(n[i]));
    }
    return answer;
}
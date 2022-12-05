function solution(n) {
    var answer = 0;
    n=String(n).split('');
    answer=n.reduce((prev,curr)=>prev+parseInt(curr),0)
    
    return answer;
}
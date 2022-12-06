function solution(i, j, k) {
    var answer = 0;
    for(let a = i;a<=j;a++){
        answer+=String(a).split('').filter(v=>v===String(k)).length;
    }
    return answer;
}
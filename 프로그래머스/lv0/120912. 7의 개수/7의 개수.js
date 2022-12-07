function solution(array) {
    var answer = 0;
    for(let i = 0; i<array.length; i++){
        answer+=String(array[i]).split('').filter((v)=>v==='7').length;
    }
    return answer;
}
function solution(cipher, code) {
    var answer = '';
    cipher.split('').map((c,i)=>(i+1)%code===0&&(answer+=c));
    return answer;
}
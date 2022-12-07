function solution(emergency) {
    var answer = [];
    const copy=[...emergency].sort((a,b)=>b-a);
    answer = emergency.map((v)=>copy.indexOf(v)+1);
    return answer;
}
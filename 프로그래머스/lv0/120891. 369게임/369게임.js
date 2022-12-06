function solution(order) {
    var answer = 0;
    String(order).split('').map((o)=>'369'.includes(o)&&(answer+=1));
    return answer;
}
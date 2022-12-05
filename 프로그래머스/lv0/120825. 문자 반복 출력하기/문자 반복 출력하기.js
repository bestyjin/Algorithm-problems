function solution(my_string, n) {
    var answer = '';
    my_string=my_string.split('');
    answer=my_string.map((s)=>s.repeat(n));
    return answer.join('');
}
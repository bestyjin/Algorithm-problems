function solution(my_string, letter) {
    var answer = '';
    my_string=my_string.split('');
    answer = my_string.filter((s)=>s!=letter);
    return answer.join('');
}
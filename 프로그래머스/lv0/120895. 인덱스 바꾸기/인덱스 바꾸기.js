function solution(my_string, num1, num2) {
    var answer = '';
    let _my_string=[...my_string];
    _my_string[num1]=my_string[num2];
    _my_string[num2]=my_string[num1];
    return _my_string.join('');
}
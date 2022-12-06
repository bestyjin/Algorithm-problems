function solution(my_string) {
    let set = new Set(my_string);
    let array = [...set];
    return array.join('');
}
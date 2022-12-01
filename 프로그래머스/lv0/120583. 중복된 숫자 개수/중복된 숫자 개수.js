function solution(array, n) {
    var answer = 0;
    let newArray = array.filter((a)=>n===a);
    answer=newArray.length;
    return answer;
}